# 15.10.2026
# Rozalia Manik (id postlink=792854)

import abc
import csv
import io
import json
import xml.etree.ElementTree as ET
from datetime import datetime


class DataExporter(abc.ABC):

    @abc.abstractmethod
    def export(self, data: list):
        """Абстрактный метод экспорта данных. Должен быть переопределен в наследниках."""
        pass

    @abc.abstractmethod
    def get_format_name(self) -> str:
        """Абстрактный метод, возвращающий имя формата экспорта."""
        pass

    def validate_data(self, data: list) -> bool:
        """Общий метод валидации: проверяет, является ли список непустым."""
        return isinstance(data, list) and len(data) > 0


class JSONExporter(DataExporter):

    def get_format_name(self) -> str:
        return "JSON"

    def export(self, data: list):
        if not self.validate_data(data):
            raise ValueError("Данные для экспорта пусты.")

        # Получаем текущее время в формате ISO 8601
        timestamp = datetime.now().isoformat()

        # Создаем глубокую копию, чтобы не менять оригинальные данные
        exported_data = []
        for record in data:
            new_record = record.copy()
            new_record["export_timestamp"] = timestamp
            exported_data.append(new_record)

        # Выводим красивый JSON в консоль
        print(json.dumps(exported_data, ensure_ascii=False, indent=2))


class CSVExporter(DataExporter):

    def get_format_name(self) -> str:
        return "CSV"

    def export(self, data: list):
        if not self.validate_data(data):
            raise ValueError("Данные для экспорта пусты.")

        # Берем заголовки из ключей первого словаря
        fieldnames = list(data[0].keys())

        # Используем StringIO, чтобы собрать CSV в памяти и вывести строкой в консоль
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=fieldnames, lineterminator="\n")

        writer.writeheader()
        writer.writerows(data)

        print(output.getvalue().strip())


class XMLExporter(DataExporter):

    def get_format_name(self) -> str:
        return "XML"

    def export(self, data: list):
        if not self.validate_data(data):
            raise ValueError("Данные для экспорта пусты.")

        # Строим дерево XML через ElementTree
        root = ET.Element("report")

        for record in data:
            item = ET.SubElement(root, "item")
            for key, val in record.items():
                child = ET.SubElement(item, key)
                child.text = str(val)

        # Преобразуем в строку с автоматическим экранированием спецсимволов (&, <, >)
        # Для форматирования отступов воспользуемся встроенной мини-утилитой indenter
        xml_string = ET.tostring(root, encoding="utf-8")
        parsed_xml = ET.XML(xml_string)
        ET.indent(parsed_xml, space="  ", level=0)

        print(ET.tostring(parsed_xml, encoding="unicode"))


# --- Пример использования по условию задачи ---
if __name__ == "__main__":
    sales_data = [
        {"product": "Laptop", "price": 1000, "quantity": 2},
        {"product": "Mouse", "price": 50, "quantity": 10},
    ]

    # Список экземпляров экспортеров
    exporters = [JSONExporter(), CSVExporter(), XMLExporter()]

    for exporter in exporters:
        # Выводим название формата строго по ТЗ
        print(f"Формат: {exporter.get_format_name()}")
        # Экспортируем данные в консоль
        exporter.export(sales_data)
        print()  # Разделительная пустая строка между форматами
