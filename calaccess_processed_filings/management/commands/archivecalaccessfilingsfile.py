#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Export and archive a .csv file for a given model.
"""
from django.apps import apps
from calaccess_processed.management.commands._archivecalaccessprocessedfile import Command as BaseCommand


class Command(BaseCommand):

    def get_model(self, processed_file):
        model_list = apps.get_app_config("calaccess_processed_filings").get_archived_models()
        model_dict = dict((m.__name__, m) for m in model_list)
        return model_dict[processed_file.file_name]