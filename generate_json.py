import datetime

fecha_actual = datetime.date.today()
hora_actual = datetime.datetime.now().time()


def generate_json(products=[], cliente_id=""):
    json_products = []

    for product in products:
        product_data = product["data"]["data"]
        sale_unit_price_rounded = round(product_data["sale_unit_price"], 2)
        purchase_unit_price_rounded = round(product_data["purchase_unit_price"], 2)
        if product["tipo_precio"] == "bodega":
            unit_price = sale_unit_price_rounded + (sale_unit_price_rounded * 0.18)
        elif product["tipo_precio"] == "mercado":
            unit_price = product_data["item_unit_types"][0]["price2"] + (
                product_data["item_unit_types"][0]["price2"] * 0.18
            )
        elif product["tipo_precio"] == "mayorista":
            unit_price = product_data["item_unit_types"][1]["price3"] + (
                product_data["item_unit_types"][1]["price3"] * 0.18
            )
        total_base_igv = product_data["sale_unit_price"] * product["cantidad"]
        total_igv = total_base_igv * 0.18

        json_products.append(
            {
                "item_id": product["id"],
                "item": {
                    "info_link": None,
                    "name_disa": "",
                    "is_set": False,
                    "laboratory": "",
                    "exportable_pharmacy": False,
                    "colors": [],
                    "shared": False,
                    "stock_by_extra": {
                        "total": -863,
                        "CatItemStatus": {"detailed": [], "total": None},
                        "CatItemUnitBusiness": {"detailed": [], "total": None},
                        "CatItemMoldCavity": {"detailed": [], "total": None},
                        "CatItemPackageMeasurement": {"detailed": [], "total": None},
                        "CatItemUnitsPerPackage": {"detailed": [], "total": None},
                        "CatItemMoldProperty": {"detailed": [], "total": None},
                        "CatItemProductFamily": {"detailed": [], "total": None},
                        "colors": {"detailed": [], "total": None},
                        "CatItemSize": {"detailed": [], "total": None},
                    },
                    "id": product["id"],
                    "sanitary": "",
                    "cod_digemid": None,
                    "unit_type_id": "NIU",
                    "unit_type_text": "Unidades",
                    "description": product_data["description"],
                    "name": None,
                    "second_name": None,
                    "model": None,
                    "barcode": product_data["barcode"],
                    "brand": "EFILA",
                    "category_description": "",
                    "warehouse_id": None,
                    "internal_id": product_data["internal_id"],
                    "item_code": None,
                    "item_code_gs1": None,
                    "stock": product_data["stock"],
                    "stock_min": "24.00",
                    "currency_type_id": "PEN",
                    "currency_type_symbol": "S/",
                    "sale_affectation_igv_type_id": "10",
                    "purchase_affectation_igv_type_id": "10",
                    "amount_sale_unit_price": str(sale_unit_price_rounded),
                    "calculate_quantity": False,
                    "has_igv": False,
                    "active": True,
                    "has_igv_description": "No",
                    "purchase_has_igv_description": "No",
                    "sale_unit_price": str(sale_unit_price_rounded),
                    "sale_unit_price_with_igv": "S/ "
                    + str(sale_unit_price_rounded * 0.18),
                    "purchase_unit_price": str(purchase_unit_price_rounded),
                    "created_at": "2021-01-14 11:44:37",  # todo asignar
                    "updated_at": "2023-09-07 11:59:12",  # todo asignar
                    "warehouses": product_data["warehouses"],
                    "apply_store": False,
                    "apply_restaurant": False,
                    "image_url": "https://melcosurdistribuciones.e.org.pe/logo/imagen-no-disponible.jpg",
                    "image_url_medium": "https://melcosurdistribuciones.e.org.pe/logo/imagen-no-disponible.jpg",
                    "image_url_small": "https://melcosurdistribuciones.e.org.pe/logo/imagen-no-disponible.jpg",
                    "tags": [],
                    "tags_id": [],
                    "item_unit_types": product_data["item_unit_types"],
                    "item_warehouse_prices": [],
                    "is_for_production": False,
                    "supplies": [],
                    "full_description": product_data["full_description"],
                    "text_filter": "",  # todo ver de donde asignar
                    "warehouse_description": "Almacén Oficina Principal",
                    "extra": {
                        "colors": None,
                        "CatItemUnitsPerPackage": None,
                        "CatItemMoldProperty": None,
                        "CatItemProductFamily": None,
                        "CatItemMoldCavity": None,
                        "CatItemPackageMeasurement": None,
                        "CatItemStatus": None,
                        "CatItemSize": None,
                        "CatItemUnitBusiness": None,
                    },
                    "category": "",
                    "purchase_has_igv": False,
                    "purchase_unit_value": product_data["purchase_unit_price"],
                    "original_unit_type_id": "NIU",
                    "sale_affectation_igv_type": {
                        "id": "10",
                        "active": 1,
                        "exportation": 0,
                        "free": 0,
                        "description": "Gravado - Operación Onerosa",
                    },
                    "has_plastic_bag_taxes": False,
                    "amount_plastic_bag_taxes": "0.50",
                    "CatItemUnitsPerPackage": [],
                    "CatItemMoldProperty": [],
                    "CatItemProductFamily": [],
                    "CatItemMoldCavity": [],
                    "CatItemPackageMeasurement": [],
                    "CatItemStatus": [],
                    "CatItemSize": [],
                    "CatItemUnitBusiness": [],
                    "attributes": [],
                    "lots_group": [],
                    "lots": [],
                    "lots_enabled": False,
                    "series_enabled": False,
                    "lot_code": None,
                    "date_of_due": None,
                    "change_free_affectation_igv": False,
                    "original_affectation_igv_type_id": "10",
                    "has_isc": False,
                    "system_isc_type_id": None,
                    "percentage_isc": "0.00",
                    "subject_to_detraction": False,
                    "exchange_points": False,
                    "quantity_of_points": 0,
                    "exchanged_for_points": False,
                    "used_points_for_exchange": None,
                    "factory_code": None,
                    "restrict_sale_cpe": False,
                    "name_product_pdf": "",
                    "unit_price": unit_price,  # TODO aca me estoy quedando
                    "presentation": {
                        "id": 1969,
                        "description": "MERCADO",
                        "item_id": 209,
                        "unit_type_id": "NIU",
                        "quantity_unit": "1.00",
                        "price1": "0.00",
                        "price2": "2.97",
                        "price3": "0.00",
                        "price_default": 2,
                        "factor_default": 0,
                        "barcode": "1969NIU1",
                    },
                },
                "currency_type_id": "PEN",
                "quantity": product["cantidad"],
                "unit_value": product_data["sale_unit_price"],  # todo: dinamico
                "affectation_igv_type_id": "10",
                "affectation_igv_type": {
                    "id": "10",
                    "active": 1,
                    "exportation": 0,
                    "free": 0,
                    "description": "Gravado - Operación Onerosa",
                },
                "total_base_igv": total_base_igv,  # 35.64  # todo: dinamico
                "percentage_igv": 18,
                "total_igv": total_igv,  # 6.42,  # todo: dinamico
                "system_isc_type_id": None,
                "total_base_isc": 0,
                "percentage_isc": 0,
                "total_isc": 0,
                "total_base_other_taxes": 0,
                "percentage_other_taxes": 0,
                "total_other_taxes": 0,
                "total_plastic_bag_taxes": 0,
                "total_taxes": total_igv,  # 6.42,  # todo: dinamico
                "price_type_id": "01",
                "unit_price": product_data["sale_unit_price"],  # unit_price es
                "input_unit_price_value": str(product["data"]["sale_unit_price"]),
                "total_value": total_base_igv,  # 35.64,  # todo: dinamico
                "total_discount": 0,
                "total_charge": 0,
                "total": product_data["sale_unit_price"]  # unit_price es
                * product["cantidad"],  # todo: dinamico
                "attributes": [],
                "charges": [],
                "discounts": [],
                "warehouse_id": None,
                "name_product_pdf": "",
                "record_id": None,
                "total_value_without_rounding": total_base_igv,  # 35.64,  # todo: dinamico
                "total_base_igv_without_rounding": total_base_igv,  # 35.64,  # todo: dinamico
                "total_igv_without_rounding": total_igv,  # 6.4152,  # todo: dinamico
                "total_taxes_without_rounding": total_igv,  # 6.4152,  # todo: dinamico
                "total_without_rounding": product_data[
                    "sale_unit_price"
                ]  # unit_price es
                * product["cantidad"],  # todo: dinamico
                "purchase_unit_price": str(
                    product_data["purchase_unit_price"]
                ),  # ,"2.40",  # todo: dinamico
                "purchase_unit_value": product_data[
                    "purchase_unit_price"
                ],  # 2.3975,  # todo: dinamico
                "purchase_has_igv": False,
                "data_item_lot_group": None,
                "IdLoteSelected": None,
                "document_item_id": None,
            }
        )

    dict_data = {
        "id": None,
        "series_id": 10,
        "prefix": "NV",
        "establishment_id": 1,
        "due_date": None,
        "date_of_issue": fecha_actual.strftime("%Y-%m-%d"),  # new Date
        "time_of_issue": hora_actual.strftime("%H:%M:%S"),  # new time
        "customer_id": cliente_id,
        "currency_type_id": "PEN",
        "purchase_order": None,
        "exchange_rate_sale": 3.708,
        "total_prepayment": 0,
        "total_charge": 0,
        "total_discount": 0,
        "total_exportation": 0,
        "total_free": 0,
        "total_taxed": 35.64,  # todo: dinamico
        "total_unaffected": 0,
        "total_exonerated": 0,
        "total_igv": 6.42,  # todo: dinamico
        "total_base_isc": 0,
        "total_isc": 0,
        "total_base_other_taxes": 0,
        "total_other_taxes": 0,
        "total_taxes": 6.42,  # todo: dinamico
        "total_value": 35.64,  # todo: dinamico
        "subtotal": 42.06,  # todo: dinamico
        "total_igv_free": 0,
        "total": 42.06,  # todo: dinamico
        "operation_type_id": None,
        "items": json_products,
        "charges": [],
        "discounts": [],
        "attributes": [],
        "guides": [],
        "payments": [],
        "additional_information": None,
        "actions": {"format_pdf": "a4"},
        "apply_concurrency": False,
        "type_period": None,
        "quantity_period": 0,
        "automatic_date_of_issue": None,
        "enabled_concurrency": False,
        "license_plate": None,
        "payment_method_type_id": None,
        "paid": False,
        "observation": None,
        "terms_condition": None,
        "cash_id": 6,
    }

    return dict_data
