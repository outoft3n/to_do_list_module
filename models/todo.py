from odoo import _, api, fields, models
from odoo.exceptions import ValidationError, UserError


class TodoListTag(models.Model):
    _name = 'todo.list.tag'
    _description = 'Todo List Tag'

    name = fields.Char('Name')
    color = fields.Integer('Color')

class TodoList(models.Model):
    _name = 'todo.list'
    _description = 'Todo List'

    title = fields.Char('Title', required=True)
    tag_ids = fields.Many2many('todo.list.tag', string='Tags')
    start_date = fields.Datetime('Start Date')
    end_date = fields.Datetime('End Date')
    status = fields.Selection([
        ('draft', 'DRAFT'),
        ('in_progress', 'IN PROGRESS'),
        ('complete', 'COMPLETE')
    ], string='status', default='draft', tracking=True)
    sub_list_ids = fields.One2many('todo.sub.list', 'todo_id', string='Sub Tasks')
    all_sub_completed = fields.Boolean(compute='_compute_all_sub_completed')
    attendee_ids = fields.One2many('todo.list.attendee', 'todo_id', string='Attendees')

    @api.depends('sub_list_ids.isComplete')
    def _compute_all_sub_completed(self):
        for record in self:
            record.all_sub_completed = record.sub_list_ids and all(sub.isComplete for sub in record.sub_list_ids)

    def action_in_progress(self):
        for record in self:
            if record.status == 'draft':
                record.status = 'in_progress'

    def action_done(self):
        for record in self:
            if record.status == 'in_progress':
                if record.all_sub_completed:
                    record.status = 'complete'
                else:
                    raise UserError("Please finished all sub tasks before proceeding.")
                
    @api.constrains('start_date', 'end_date')
    def _check_date(self):
        for record in self:
            if record.start_date and record.end_date and record.start_date > record.end_date:
                raise ValidationError('End date cannot be earlier than the start date.')

class TodoSubList(models.Model):
    _name = 'todo.sub.list'
    _description = 'Todo Sub List'

    todo_id = fields.Many2one('todo.list', string='Parent Todo', ondelete='cascade')
    title = fields.Char('title')
    description = fields.Text('description')
    isComplete = fields.Boolean('isComplete')
    parent_status = fields.Selection(related='todo_id.status', store=False)

class TodoAttendee(models.Model):
    _name = 'todo.list.attendee'
    _description = 'Todo List Attendee'

    todo_id = fields.Many2one('todo.list', string='Parent Todo', ondelete='cascade')
    user_id = fields.Many2one('res.users', string='Attendee', required=True)
    parent_status = fields.Selection(related='todo_id.status', store=False)
    