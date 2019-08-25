from .documents import FinalProductDocument


class FinalProductService:
    @staticmethod
    def get_all():
        return FinalProductDocument.search().execute().to_dict()["hits"]["hits"]

    @staticmethod
    def get_less_than_quantity_stock(quantity_in_stock):
        return (
            FinalProductDocument.search()
            .filter("range", quantity_in_stock={"lte": quantity_in_stock})
            .execute()
            .to_dict()["hits"]["hits"]
        )
