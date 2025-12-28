# To-Do List Management Module for Odoo

An Odoo module designed to streamline task management, categorize activities with tags, and ensure process integrity through sub-task validation.

## Installation & Setup

1.  Copy the module folder into your Odoo `addons` directory.
2.  Update the App List in your Odoo instance.
3.  Acitvate the module

## How to Use

1.  **Create**: Click **New** to start a task; it defaults to **Draft** status.
2.  **Define**: Enter the Title, select Tags, and set your dates.
3.  **Detail**: Add specific steps in the Sub-tasks table at the bottom.
4.  **Execute**: Click the **PROGRESS** button to move to **In Progress**.
5.  **Finish**: Mark all sub-tasks as `isComplete`, then click **PROGRESS** again to finalize the task as **Complete**.

## Menu Views

The module provides 3 filtered views for better task organization
* **Todo list**: Displays every record created in the system, providing a comprehensive overview of all tasks.
* **Todo list uncomplete**: Displays only those records where the status is **NOT** set to 'Complete'.
* **Todo list complete**: Displays only the records that have successfully reached the **'Complete'** status.

---
Developed by: `Natnicha U. (outoft3n)`
