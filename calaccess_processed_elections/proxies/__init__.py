#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Proxy models for augmenting our source data tables with methods useful for processing.
"""
from .opencivicdata import (
    OCDBallotMeasureContestProxy,
    OCDBallotMeasureContestIdentifierProxy,
    OCDBallotMeasureContestOptionProxy,
    OCDBallotMeasureContestSourceProxy,
    OCDCandidateContestProxy,
    OCDCandidateContestPostProxy,
    OCDCandidateContestSourceProxy,
    OCDCandidacyProxy,
    OCDCandidacySourceProxy,
    OCDElectionProxy,
    OCDElectionIdentifierProxy,
    OCDElectionSourceProxy,
    OCDPartyProxy,
    OCDRetentionContestProxy,
    OCDRetentionContestIdentifierProxy,
    OCDRetentionContestOptionProxy,
    OCDRetentionContestSourceProxy,
    OCDDivisionProxy,
    OCDMembershipProxy,
    OCDJurisdictionProxy,
    OCDOrganizationProxy,
    OCDOrganizationIdentifierProxy,
    OCDOrganizationNameProxy,
    OCDPersonProxy,
    OCDPersonIdentifierProxy,
    OCDPersonNameProxy,
    OCDPostProxy
)
from .calaccess_raw import RawFilerToFilerTypeCdProxy
from .calaccess_scraped import (
    ScrapedElectionProxyMixin,
    ScrapedNameMixin,
    ScrapedCandidateProxy,
    ScrapedIncumbentProxy,
    ScrapedCandidateElectionProxy,
    ScrapedIncumbentElectionProxy,
    ScrapedPropositionProxy,
    ScrapedPropositionElectionProxy
)


__all__ = (
    "OCDBallotMeasureContestProxy",
    "OCDBallotMeasureContestIdentifierProxy",
    "OCDBallotMeasureContestOptionProxy",
    "OCDBallotMeasureContestSourceProxy",
    "OCDCandidateContestProxy",
    "OCDCandidateContestPostProxy",
    "OCDCandidateContestSourceProxy",
    "OCDCandidacyProxy",
    "OCDCandidacySourceProxy",
    "OCDElectionProxy",
    "OCDElectionIdentifierProxy",
    "OCDElectionSourceProxy",
    "OCDPartyProxy",
    "OCDRetentionContestProxy",
    "OCDRetentionContestIdentifierProxy",
    "OCDRetentionContestOptionProxy",
    "OCDRetentionContestSourceProxy",
    'OCDDivisionProxy',
    'OCDJurisdictionProxy',
    'OCDMembershipProxy',
    'OCDOrganizationProxy',
    'OCDOrganizationIdentifierProxy',
    'OCDOrganizationNameProxy',
    'OCDPersonProxy',
    'OCDPersonIdentifierProxy',
    'OCDPersonNameProxy',
    'OCDPostProxy',
    "RawFilerToFilerTypeCdProxy",
    "ScrapedElectionProxyMixin",
    "ScrapedNameMixin",
    'ScrapedCandidateProxy',
    'ScrapedCandidateElectionProxy',
    'ScrapedIncumbentProxy',
    'ScrapedIncumbentElectionProxy',
    'ScrapedPropositionProxy',
    'ScrapedPropositionElectionProxy',
)