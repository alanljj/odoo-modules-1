Colored field widget
====================

Module provides widgets to color some fields in **ListView**.

.. raw:: html

    <style> .warning {color:red; font-weight:bold;} </style>

.. role:: warning

Colored Widget
--------------

Widget allows you to color fields based on condition.

To use this widget, you must set some attributes in field definition. Can be used for all fields, that are displayed
as text.

.. code-block:: xml

    <field name="name" widget="colored" check="mark_color" hover_title="type_id"/>

:check: if this field has value and it's value si not False, original field will be colored.
:hover_title: (optional) define field, which text will be used for tooltip instead of field help text.
:color: (optional) define color, that will be used to color field. Default value is :warning:`red`.
:other_style: (optional) define other text, that will be used in style attribute. Default value is empty.

Colored Boolean Widget
----------------------

Widget allows you to add colored text to selection field based on condition.

To use this widget, you must set some attributes in field definition. Can be used for boolean fields.

.. code-block:: xml

    <field name="is_currency" widget="bool_colored" check="old_is_currency" hover_title="old_is_currency"  color="blue" check_text="Changed"/>

:check: if this field has value and it's value si not False, original field will be colored.
:check_text: text, that will be displayed, when condition is true
:hover_title: (optional) define field, which text will be used for tooltip instead of field help text.
:color: (optional) define color, that will be used to color field. Default value is *:warning:`red`.
:other_style: (optional) define other text, that will be used in style attribute. Default value is empty.
