#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Load data from CAL-ACCESS' Form 460 into standardized OCD models.
"""
from calaccess_processed import models
from calaccess_processed.management.commands import CalAccessCommand


class Command(CalAccessCommand):
    """
    Load data from CAL-ACCESS' Form 460 into standardized OCD models.
    """
    help = "Load data from CAL-ACCESS' Form 460 into standardized OCD models."

    def add_arguments(self, parser):
        """
        Adds custom arguments specific to this command.
        """
        parser.add_argument(
            "--flush",
            action="store_true",
            dest="flush",
            default=False,
            help="Flush OCD filing models prior to loading"
        )

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        super(Command, self).handle(*args, **options)
        if options['flush']:
            self.flush()
        self.load()

    def flush(self, *args, **kwargs):
        """
        Clear out the OCD models loaded by this command.
        """
        self.header('Flushing OCD data extracted from Form 460 filings')
        model_list = [
            models.OCDTransactionProxy,
            models.OCDFilingActionSummaryAmountProxy,
            models.OCDFilingActionProxy,
            models.OCDFilingProxy,
            models.OCDFilingIdentifierProxy,
            models.OCDCommitteeProxy,
            models.OCDCommitteeIdentifierProxy,
            models.OCDCommitteeNameProxy,
            models.OCDCommitteeTypeProxy,
        ]
        for m in model_list:
            self.log(" Flushing {}".format(m.__name__))
            m.objects.all().delete()

    def load_model(self, model):
        """
        Loads the provided model.
        """
        self.log('  Loading {}'.format(model.__name__))
        before = model.objects.count()
        model.objects.load_form460_data()
        after = model.objects.count()
        self.log('   {:,} added'.format(after-before))

    def load(self, *args, **kwargs):
        """
        Load data from Form 460 models into OCD models.
        """
        self.header('Loading data extracted from Form 460 filings')

        if not models.OCDCommitteeTypeProxy.objects.exists():
            self.log(' Creating committee types')
            models.OCDCommitteeTypeProxy.objects.seed()

        #
        # Committees
        #

        self.log(' Updating committee roster')
        self.load_model(models.OCDCommitteeProxy)
        self.load_model(models.OCDCommitteeIdentifierProxy)
        self.load_model(models.OCDCommitteeNameProxy)

        #
        # Filings
        #

        self.load_model(models.OCDFilingProxy)
        self.load_model(models.OCDFilingIdentifierProxy)

        #
        # Filing actions
        #

        self.load_model(models.OCDFilingActionProxy)
        self.load_model(models.OCDFilingActionSummaryAmountProxy)

        #
        # Transactions
        #

        self.load_model(models.OCDTransactionProxy)
