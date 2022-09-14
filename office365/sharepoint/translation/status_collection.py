from office365.runtime.client_value_collection import ClientValueCollection
from office365.runtime.queries.service_operation import ServiceOperationQuery
from office365.runtime.types.collections import StringCollection
from office365.sharepoint.base_entity import BaseEntity
from office365.sharepoint.translation.status import TranslationStatus
from office365.sharepoint.translation.status_set_request import TranslationStatusSetRequest


class TranslationStatusCollection(BaseEntity):

    def __init__(self, context, resource_path=None):
        super(TranslationStatusCollection, self).__init__(context, resource_path)

    def set(self):
        return_type = TranslationStatusCollection(self.context)
        request = TranslationStatusSetRequest()
        qry = ServiceOperationQuery(self, "Set", None, request, None, return_type)
        self.context.add_query(qry)
        return return_type

    @property
    def untranslated_languages(self):
        return self.properties.get("UntranslatedLanguages", StringCollection())

    @property
    def items(self):
        return self.properties.get("Items", ClientValueCollection(TranslationStatus))
