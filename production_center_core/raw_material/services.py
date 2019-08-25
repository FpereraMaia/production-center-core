from .documents import RawMaterialDocument


class RawMaterialService:
    @staticmethod
    def get_all():
        return RawMaterialDocument.search().execute().to_dict()["hits"]["hits"]

    @staticmethod
    def get_less_than_quantity_stock(quantity_in_stock):
        return (
            RawMaterialDocument.search()
            .filter("range", quantity_in_stock={"lte": quantity_in_stock})
            .execute()
            .to_dict()["hits"]["hits"]
        )
