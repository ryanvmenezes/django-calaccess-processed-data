#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Proxy models for augmenting our source data tables with methods useful for processing.
"""
from .calaccess_raw import RawFilerToFilerTypeCdManager
from .calaccess_scraped import (
    ScrapedCandidateProxy,
    ScrapedIncumbentProxy,
    ScrapedCandidateElectionProxy,
    ScrapedIncumbentElectionProxy,
    ScrapedPropositionProxy,
    ScrapedPropositionElectionProxy
)
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
    OCDDivisionProxy,
    OCDElectionProxy,
    OCDElectionIdentifierProxy,
    OCDElectionSourceProxy,
    OCDMembershipProxy,
    OCDOrganizationProxy,
    OCDOrganizationIdentifierProxy,
    OCDOrganizationNameProxy,
    OCDPartyProxy,
    OCDPersonProxy,
    OCDPersonNameProxy,
    OCDPostProxy,
    OCDProxyModelMixin,
    OCDRetentionContestProxy,
    OCDRetentionContestIdentifierProxy,
    OCDRetentionContestOptionProxy,
    OCDRetentionContestSourceProxy,
)


__all__ = (
    'RawFilerToFilerTypeCdManager',
    'ScrapedCandidateProxy',
    'ScrapedCandidateElectionProxy',
    'ScrapedIncumbentProxy',
    'ScrapedIncumbentElectionProxy',
    'ScrapedPropositionProxy',
    'ScrapedPropositionElectionProxy',
    'OCDBallotMeasureContestProxy',
    'OCDBallotMeasureContestIdentifierProxy',
    'OCDBallotMeasureContestOptionProxy',
    'OCDBallotMeasureContestSourceProxy',
    'OCDCandidateContestProxy',
    'OCDCandidateContestPostProxy',
    'OCDCandidateContestSourceProxy',
    'OCDCandidacyProxy',
    'OCDCandidacySourceProxy',
    'OCDDivisionProxy',
    'OCDElectionProxy',
    'OCDElectionIdentifierProxy',
    'OCDElectionSourceProxy',
    'OCDMembershipProxy',
    'OCDOrganizationProxy',
    'OCDOrganizationIdentifierProxy',
    'OCDOrganizationNameProxy',
    'OCDPartyProxy',
    'OCDPersonProxy',
    'OCDPersonNameProxy',
    'OCDPostProxy',
    'OCDProxyModelMixin',
    'OCDRetentionContestProxy',
    'OCDRetentionContestIdentifierProxy',
    'OCDRetentionContestOptionProxy',
    'OCDRetentionContestSourceProxy',
)
