def generate_json(products=[]):
    json_products = []

    for product in products:
        json_products.append(
            {
                "item_id": product["id"],
                "item": product,
                "currency_type_id": "PEN",
                "quantity": "12",  # todo: dinamico
                "unit_value": 2.97,  # todo: dinamico
                "affectation_igv_type_id": "10",
                "affectation_igv_type": {
                    "id": "10",
                    "active": 1,
                    "exportation": 0,
                    "free": 0,
                    "description": "Gravado - Operación Onerosa",
                },
                "total_base_igv": 35.64,  # todo: dinamico
                "percentage_igv": 18,
                "total_igv": 6.42,  # todo: dinamico
                "system_isc_type_id": None,
                "total_base_isc": 0,
                "percentage_isc": 0,
                "total_isc": 0,
                "total_base_other_taxes": 0,
                "percentage_other_taxes": 0,
                "total_other_taxes": 0,
                "total_plastic_bag_taxes": 0,
                "total_taxes": 6.42,  # todo: dinamico
                "price_type_id": "01",
                "unit_price": 3.5046,  # todo: dinamico
                "input_unit_price_value": "2.97",
                "total_value": 35.64,  # todo: dinamico
                "total_discount": 0,
                "total_charge": 0,
                "total": 42.06,  # todo: dinamico
                "attributes": [],
                "charges": [],
                "discounts": [],
                "warehouse_id": None,
                "name_product_pdf": "",
                "record_id": None,
                "total_value_without_rounding": 35.64,  # todo: dinamico
                "total_base_igv_without_rounding": 35.64,  # todo: dinamico
                "total_igv_without_rounding": 6.4152,  # todo: dinamico
                "total_taxes_without_rounding": 6.4152,  # todo: dinamico
                "total_without_rounding": 42.0552,  # todo: dinamico
                "purchase_unit_price": "2.40",  # todo: dinamico
                "purchase_unit_value": 2.3975,  # todo: dinamico
                "purchase_has_igv": False,
                "data_item_lot_group": None,
                "IdLoteSelected": None,
                "document_item_id": None,
            }
        )

    dict_data = {
        "nombre": "Arnold Olanda Muñoz",  # eliminar
        "direccion": "Alto Paucarpata A-2",  # eliminar
        "tipo_cliente": "mayorista",  # eliminar
        "id": None,
        "series_id": 10,
        "prefix": "NV",
        "establishment_id": 1,
        "due_date": None,
        "date_of_issue": "2023-09-07",  # new Date
        "time_of_issue": "13:20:05",  # new time
        "customer_id": 2192,  # todo: dinamico
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
