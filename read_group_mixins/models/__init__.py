#-*- coding:utf-8 -*-

from openerp import models, fields, api


class ComputeFieldMixin(models.Model):

    _name = 'read_group_mixin.compute_field'

    _field_compute_list = []

    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, context=None, orderby=False, lazy=True,
                   **kwargs):
        """
        Overrided to add some computed field to group line
        """
        res = super(ComputeFieldMixin, self).read_group(domain, fields, groupby, offset, limit=limit,
                                                  context=context, orderby=orderby, lazy=lazy, **kwargs)
        for line in res:
            result = self.search(line.get('__domain', []))
            for field in self._field_compute_list:
                line[field] = sum(result.mapped(field))
        return res


class GroupResultApplyMixin(models.Model):

    _name = 'read_group_mixin.group_result_apply'

    @api.model
    def process_read_group_result(self, result):
        pass

    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, context=None, orderby=False, lazy=True,
                   **kwargs):
        """
        Overrided
        overrided to add custom logic
        """
        res = super(GroupResultApplyMixin, self).read_group(domain, fields, groupby, offset, limit=limit,
                                                 context=context, orderby=orderby, lazy=lazy, **kwargs)
        res = self.process_read_group_result(res)
        if not res:
            raise Exception('You must override process_read_group_result method to use group_result_apply mixin')
        return res
