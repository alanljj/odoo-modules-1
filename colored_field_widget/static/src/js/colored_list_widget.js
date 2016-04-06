openerp.colored_field_widget = function (instance, local) {
    local.ColoredField = instance.web.list.Column.extend({
        get_style: function (row_data) {
            var check_value = row_data[this.check];
            var color = this.color ? this.color : 'red';
            if (check_value && check_value.value != false) {
                return 'color: ' + color + ';' + (this.other_style || '');
            }
            return this.other_style || '';
        },
        /* alternative title*/
        get_title: function (row_data) {
            var title_value = row_data[this.hover_title];
            if (typeof title_value !== "undefined" && title_value) {
                return title_value;
            } else {
                return this.help;
            }
        },
        /**
         * Override _format function due to strange format logic in odoo
         * Odoo search formatting method by widget name or widget type or else.
         * So, I must remove widget name because this widget don't have formatting style in odoo
         * For details: addons/web/static/src/js/formats.js:156
         */
        _format: function (row_data, options) {
            return _.escape(instance.web.format_value(
                row_data[this.id].value, {type: this.type}, options.value_if_empty));
        }
    });

    local.ColoredBooleanField = instance.web.list.Boolean.extend({
        get_style: function (row_data) {
            var check_value = row_data[this.check];
            var color = this.color ? this.color : 'red';
            if (check_value && check_value.value != false) {
                return 'color: ' + color + ';' + (this.other_style || '');
            }
            return this.other_style || '';
        },
        /* alternative title*/
        get_title: function (row_data) {
            var title_value = row_data[this.hover_title];
            if (typeof title_value !== "undefined" && title_value) {
                return title_value;
            } else {
                return this.help;
            }
        },

        _format: function (row_data, options) {
            return _.str.sprintf('<input type="checkbox" %s readonly="readonly"/>%s',
                row_data[this.id].value ? 'checked="checked"' : '', row_data[this.check].value ? this.check_text: '');
        }
    });


    instance.web.list.columns.add('field.colored', 'instance.colored_field_widget.ColoredField');
    instance.web.list.columns.add('field.bool_colored', 'instance.colored_field_widget.ColoredBooleanField');
};
