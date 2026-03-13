from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

from xsdata.models.datatype import XmlDate, XmlDateTime

from xsdata_ech.e_ch_0044_4_1 import SexType
from xsdata_ech.e_ch_0058_5_0 import HeaderType
from xsdata_ech.e_ch_0155_5_2 import (
    CandidateType,
    DomainOfInfluenceType,
    DomainOfInfluenceTypeType,
    ElectionType,
    ExtensionType,
    ListType,
    ListUnionType,
    VoterTypeType,
)

__NAMESPACE__ = "http://www.ech.ch/xmlns/eCH-0252/2"


@dataclass(kw_only=True)
class CandidateListResultType:
    class Meta:
        name = "candidateListResultType"

    list_identification: str = field(
        metadata={
            "name": "listIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 50,
        }
    )
    count_of_votes_from_changed_ballots: int = field(
        metadata={
            "name": "countOfVotesFromChangedBallots",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        }
    )


class DecisiveMajorityType(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


@dataclass(kw_only=True)
class ElectionAssociationDescriptionInformationType:
    class Meta:
        name = "electionAssociationDescriptionInformationType"

    language: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "length": 2,
        }
    )
    election_association_description_short: None | str = field(
        default=None,
        metadata={
            "name": "electionAssociationDescriptionShort",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 100,
        },
    )
    election_association_description: str = field(
        metadata={
            "name": "electionAssociationDescription",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 255,
        }
    )


@dataclass(kw_only=True)
class ListOrListUnionIdentificationType:
    class Meta:
        name = "listOrListUnionIdentificationType"

    list_identification: None | str = field(
        default=None,
        metadata={
            "name": "listIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 50,
        },
    )
    list_union_identification: None | str = field(
        default=None,
        metadata={
            "name": "listUnionIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 50,
        },
    )


class MandateTypeTypeMandateTypeFix(Enum):
    VALUE_1 = 1
    VALUE_2 = 2


class MandateTypeTypeMandateTypeOther(Enum):
    VALUE_3 = 3


@dataclass(kw_only=True)
class NamedElementType:
    class Meta:
        name = "namedElementType"

    element_name: str = field(
        metadata={
            "name": "elementName",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 100,
        }
    )
    count_of: None | int = field(
        default=None,
        metadata={
            "name": "countOf",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        },
    )
    percent: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("100.00"),
            "total_digits": 5,
            "fraction_digits": 2,
        },
    )
    text: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 500,
        },
    )
    decimal: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )


@dataclass(kw_only=True)
class NamedIdType:
    class Meta:
        name = "namedIdType"

    id_name: str = field(
        metadata={
            "name": "idName",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 20,
        }
    )
    id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 50,
        }
    )


class VoteSubTypeType(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


@dataclass(kw_only=True)
class VoteTitleInformationType:
    class Meta:
        name = "voteTitleInformationType"

    language: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "length": 2,
        }
    )
    vote_title: str = field(
        metadata={
            "name": "voteTitle",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 700,
        }
    )
    vote_title_short: None | str = field(
        default=None,
        metadata={
            "name": "voteTitleShort",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 300,
        },
    )


@dataclass(kw_only=True)
class VotingCardInformationType:
    class Meta:
        name = "votingCardInformationType"

    count_of_voting_cards_received_in_ballot_box: None | int = field(
        default=None,
        metadata={
            "name": "countOfVotingCardsReceivedInBallotBox",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        },
    )
    count_of_voting_cards_received_prematurely_in_ballot_box: None | int = (
        field(
            default=None,
            metadata={
                "name": "countOfVotingCardsReceivedPrematurelyInBallotBox",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_inclusive": 0,
                "max_inclusive": 9999999,
            },
        )
    )
    count_of_voting_cards_received_by_mail: None | int = field(
        default=None,
        metadata={
            "name": "countOfVotingCardsReceivedByMail",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        },
    )
    count_of_invalid_voting_cards_received_by_mail: None | int = field(
        default=None,
        metadata={
            "name": "countOfInvalidVotingCardsReceivedByMail",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        },
    )
    count_of_voting_cards_received_by_evoting: None | int = field(
        default=None,
        metadata={
            "name": "countOfVotingCardsReceivedByEvoting",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        },
    )


@dataclass(kw_only=True)
class CandidateOrWriteInCandidateType:
    class Meta:
        name = "candidateOrWriteInCandidateType"

    candidate_identification: None | str = field(
        default=None,
        metadata={
            "name": "candidateIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 50,
        },
    )
    candidate_reference: None | str = field(
        default=None,
        metadata={
            "name": "candidateReference",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 10,
        },
    )
    write_in_candidate: None | CandidateType = field(
        default=None,
        metadata={
            "name": "writeInCandidate",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )


@dataclass(kw_only=True)
class CountOfVotersInformationType:
    class Meta:
        name = "countOfVotersInformationType"

    count_of_voters_total: int = field(
        metadata={
            "name": "countOfVotersTotal",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        }
    )
    subtotal_info: list[CountOfVotersInformationType.SubtotalInfo] = field(
        default_factory=list,
        metadata={
            "name": "subtotalInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )

    @dataclass(kw_only=True)
    class SubtotalInfo:
        count_of_voters: int = field(
            metadata={
                "name": "countOfVoters",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_inclusive": 0,
                "max_inclusive": 9999999,
            }
        )
        voter_type: None | VoterTypeType = field(
            default=None,
            metadata={
                "name": "voterType",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )
        sex: None | SexType = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )
        is_minor: None | bool = field(
            default=None,
            metadata={
                "name": "isMinor",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )
        named_element: list[NamedElementType] = field(
            default_factory=list,
            metadata={
                "name": "namedElement",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )


@dataclass(kw_only=True)
class CountingCircleType:
    class Meta:
        name = "countingCircleType"

    counting_circle_id: None | str = field(
        default=None,
        metadata={
            "name": "countingCircleId",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 50,
        },
    )
    counting_circle_name: None | str = field(
        default=None,
        metadata={
            "name": "countingCircleName",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 100,
        },
    )
    domain_of_influence_type: None | DomainOfInfluenceTypeType = field(
        default=None,
        metadata={
            "name": "domainOfInfluenceType",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )


@dataclass(kw_only=True)
class ElectionAssociationType:
    class Meta:
        name = "electionAssociationType"

    election_association_id: str = field(
        metadata={
            "name": "electionAssociationId",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 50,
        }
    )
    election_association_description: list[
        ElectionAssociationDescriptionInformationType
    ] = field(
        default_factory=list,
        metadata={
            "name": "electionAssociationDescription",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_occurs": 1,
        },
    )
    quorum: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("100.00"),
            "total_digits": 5,
            "fraction_digits": 2,
        },
    )
    named_element: list[NamedElementType] = field(
        default_factory=list,
        metadata={
            "name": "namedElement",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )


@dataclass(kw_only=True)
class ListResultType:
    class Meta:
        name = "listResultType"

    list_identification: str = field(
        metadata={
            "name": "listIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 50,
        }
    )
    list_indenture_number: None | str = field(
        default=None,
        metadata={
            "name": "listIndentureNumber",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 6,
        },
    )
    count_of_changed_ballots: int = field(
        metadata={
            "name": "countOfChangedBallots",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        }
    )
    count_of_unchanged_ballots: int = field(
        metadata={
            "name": "countOfUnchangedBallots",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        }
    )
    count_of_candidate_votes: int = field(
        metadata={
            "name": "countOfCandidateVotes",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        }
    )
    count_of_additional_votes: int = field(
        metadata={
            "name": "countOfAdditionalVotes",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        }
    )
    candidate_results: list[ListResultType.CandidateResults] = field(
        default_factory=list,
        metadata={
            "name": "candidateResults",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_occurs": 1,
        },
    )
    named_element: list[NamedElementType] = field(
        default_factory=list,
        metadata={
            "name": "namedElement",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )

    @dataclass(kw_only=True)
    class CandidateResults:
        """
        :ivar candidate_identification:
        :ivar candidate_reference_on_position:
        :ivar count_of_votes_from_changed_ballots:
        :ivar count_of_votes_from_unchanged_ballots:
        :ivar candidate_list_results_info: The element is only
            transmitted if this has been agreed by the sender and
            recipient. Once it has been used, it must always be
            transmitted.
        :ivar named_element:
        """

        candidate_identification: str = field(
            metadata={
                "name": "candidateIdentification",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_length": 1,
                "max_length": 50,
            }
        )
        candidate_reference_on_position: list[str] = field(
            default_factory=list,
            metadata={
                "name": "candidateReferenceOnPosition",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_length": 1,
                "max_length": 10,
            },
        )
        count_of_votes_from_changed_ballots: int = field(
            metadata={
                "name": "countOfVotesFromChangedBallots",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_inclusive": 0,
                "max_inclusive": 9999999,
            }
        )
        count_of_votes_from_unchanged_ballots: int = field(
            metadata={
                "name": "countOfVotesFromUnchangedBallots",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_inclusive": 0,
                "max_inclusive": 9999999,
            }
        )
        candidate_list_results_info: (
            None | ListResultType.CandidateResults.CandidateListResultsInfo
        ) = field(
            default=None,
            metadata={
                "name": "candidateListResultsInfo",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )
        named_element: list[NamedElementType] = field(
            default_factory=list,
            metadata={
                "name": "namedElement",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )

        @dataclass(kw_only=True)
        class CandidateListResultsInfo:
            candidate_list_results: list[CandidateListResultType] = field(
                default_factory=list,
                metadata={
                    "name": "candidateListResults",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )
            count_of_votes_from_ballots_without_list_designation: (
                None | int
            ) = field(
                default=None,
                metadata={
                    "name": "countOfVotesFromBallotsWithoutListDesignation",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                    "min_inclusive": 0,
                    "max_inclusive": 9999999,
                },
            )
            named_element: list[NamedElementType] = field(
                default_factory=list,
                metadata={
                    "name": "namedElement",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )


@dataclass(kw_only=True)
class MandateTypeType:
    class Meta:
        name = "mandateTypeType"

    mandate_type_fix: None | MandateTypeTypeMandateTypeFix = field(
        default=None,
        metadata={
            "name": "mandateTypeFix",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )
    mandate_type_other: None | MandateTypeTypeMandateTypeOther = field(
        default=None,
        metadata={
            "name": "mandateTypeOther",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )
    mandate_type_info: list[MandateTypeType.MandateTypeInfo] = field(
        default_factory=list,
        metadata={
            "name": "mandateTypeInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )

    @dataclass(kw_only=True)
    class MandateTypeInfo:
        language: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            }
        )
        mandate_type_description: None | object = field(
            default=None,
            metadata={
                "name": "mandateTypeDescription",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )


@dataclass(kw_only=True)
class VoteResultDataType:
    class Meta:
        name = "voteResultDataType"

    percent_of_yes_votes: Decimal = field(
        metadata={
            "name": "percentOfYesVotes",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("100.00"),
            "total_digits": 5,
            "fraction_digits": 2,
        }
    )
    percent_of_no_votes: Decimal = field(
        metadata={
            "name": "percentOfNoVotes",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("100.00"),
            "total_digits": 5,
            "fraction_digits": 2,
        }
    )
    named_element: list[NamedElementType] = field(
        default_factory=list,
        metadata={
            "name": "namedElement",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )


@dataclass(kw_only=True)
class VoteType:
    class Meta:
        name = "voteType"

    vote_identification: str = field(
        metadata={
            "name": "voteIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 50,
        }
    )
    main_vote_identification: None | str = field(
        default=None,
        metadata={
            "name": "mainVoteIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 50,
        },
    )
    other_identification: list[NamedIdType] = field(
        default_factory=list,
        metadata={
            "name": "otherIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )
    domain_of_influence: DomainOfInfluenceType = field(
        metadata={
            "name": "domainOfInfluence",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        }
    )
    superior_authority: None | DomainOfInfluenceType = field(
        default=None,
        metadata={
            "name": "superiorAuthority",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )
    polling_day: XmlDate = field(
        metadata={
            "name": "pollingDay",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        }
    )
    vote_title_information: list[VoteTitleInformationType] = field(
        default_factory=list,
        metadata={
            "name": "voteTitleInformation",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_occurs": 1,
        },
    )
    decisive_majority: DecisiveMajorityType = field(
        metadata={
            "name": "decisiveMajority",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        }
    )
    vote_sub_type: VoteSubTypeType = field(
        metadata={
            "name": "voteSubType",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        }
    )
    sequence: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 1,
            "max_inclusive": 999,
        },
    )
    grouping: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 50,
        },
    )
    named_element: list[NamedElementType] = field(
        default_factory=list,
        metadata={
            "name": "namedElement",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )


@dataclass(kw_only=True)
class CandidateResultType:
    class Meta:
        name = "candidateResultType"

    candidate_or_write_in_candidate: CandidateOrWriteInCandidateType = field(
        metadata={
            "name": "candidateOrWriteInCandidate",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        }
    )
    count_of_votes_total: int = field(
        metadata={
            "name": "countOfVotesTotal",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        }
    )
    candidate_list_results_info: (
        None | CandidateResultType.CandidateListResultsInfo
    ) = field(
        default=None,
        metadata={
            "name": "candidateListResultsInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )

    @dataclass(kw_only=True)
    class CandidateListResultsInfo:
        candidate_list_results: list[CandidateListResultType] = field(
            default_factory=list,
            metadata={
                "name": "candidateListResults",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )
        count_of_votes_from_ballots_without_list_designation: None | int = (
            field(
                default=None,
                metadata={
                    "name": "countOfVotesFromBallotsWithoutListDesignation",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                    "min_inclusive": 0,
                    "max_inclusive": 9999999,
                },
            )
        )


@dataclass(kw_only=True)
class DrawElectionType:
    class Meta:
        name = "drawElectionType"

    majority_election: None | DrawElectionType.MajorityElection = field(
        default=None,
        metadata={
            "name": "majorityElection",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )
    proportional_election: None | DrawElectionType.ProportionalElection = (
        field(
            default=None,
            metadata={
                "name": "proportionalElection",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )
    )

    @dataclass(kw_only=True)
    class MajorityElection:
        is_draw_pending: bool = field(
            metadata={
                "name": "isDrawPending",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            }
        )
        candidate_draw_election: list[CandidateOrWriteInCandidateType] = field(
            default_factory=list,
            metadata={
                "name": "candidateDrawElection",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_occurs": 2,
            },
        )
        winning_candidate: list[CandidateOrWriteInCandidateType] = field(
            default_factory=list,
            metadata={
                "name": "winningCandidate",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )
        named_element: list[NamedElementType] = field(
            default_factory=list,
            metadata={
                "name": "namedElement",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )

    @dataclass(kw_only=True)
    class ProportionalElection:
        list_or_list_union_draw_election: list[
            DrawElectionType.ProportionalElection.ListOrListUnionDrawElection
        ] = field(
            default_factory=list,
            metadata={
                "name": "listOrListUnionDrawElection",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )
        candidate_draw_election_on_list: list[
            DrawElectionType.ProportionalElection.CandidateDrawElectionOnList
        ] = field(
            default_factory=list,
            metadata={
                "name": "candidateDrawElectionOnList",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )

        @dataclass(kw_only=True)
        class ListOrListUnionDrawElection:
            is_draw_pending: bool = field(
                metadata={
                    "name": "isDrawPending",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                }
            )
            list_or_list_union_identification: list[
                ListOrListUnionIdentificationType
            ] = field(
                default_factory=list,
                metadata={
                    "name": "listOrListUnionIdentification",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                    "min_occurs": 2,
                },
            )
            winning_list_or_list_union_identification: list[
                ListOrListUnionIdentificationType
            ] = field(
                default_factory=list,
                metadata={
                    "name": "winningListOrListUnionIdentification",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )
            named_element: list[NamedElementType] = field(
                default_factory=list,
                metadata={
                    "name": "namedElement",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )

        @dataclass(kw_only=True)
        class CandidateDrawElectionOnList:
            is_draw_pending: bool = field(
                metadata={
                    "name": "isDrawPending",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                }
            )
            list_identification: str = field(
                metadata={
                    "name": "listIdentification",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                    "min_length": 1,
                    "max_length": 50,
                }
            )
            candidate_identification: list[str] = field(
                default_factory=list,
                metadata={
                    "name": "candidateIdentification",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                    "min_occurs": 2,
                    "min_length": 1,
                    "max_length": 50,
                },
            )
            winning_candidate_identification: list[str] = field(
                default_factory=list,
                metadata={
                    "name": "winningCandidateIdentification",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                    "min_length": 1,
                    "max_length": 50,
                },
            )
            named_element: list[NamedElementType] = field(
                default_factory=list,
                metadata={
                    "name": "namedElement",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )


@dataclass(kw_only=True)
class ElectedType:
    class Meta:
        name = "electedType"

    majority_election: None | ElectedType.MajorityElection = field(
        default=None,
        metadata={
            "name": "majorityElection",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )
    proportional_election: None | ElectedType.ProportionalElection = field(
        default=None,
        metadata={
            "name": "proportionalElection",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )

    @dataclass(kw_only=True)
    class MajorityElection:
        absolute_majority: None | int = field(
            default=None,
            metadata={
                "name": "absoluteMajority",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_inclusive": 0,
                "max_inclusive": 9999999,
            },
        )
        is_election_result_complete: bool = field(
            metadata={
                "name": "isElectionResultComplete",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            }
        )
        elected_candidate: list[
            ElectedType.MajorityElection.ElectedCandidate
        ] = field(
            default_factory=list,
            metadata={
                "name": "electedCandidate",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )

        @dataclass(kw_only=True)
        class ElectedCandidate:
            candidate_or_write_in_candidate: CandidateOrWriteInCandidateType = field(
                metadata={
                    "name": "candidateOrWriteInCandidate",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                }
            )
            is_elected_by_draw: None | bool = field(
                default=None,
                metadata={
                    "name": "isElectedByDraw",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )
            sort_id: None | int = field(
                default=None,
                metadata={
                    "name": "sortID",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )
            named_element: list[NamedElementType] = field(
                default_factory=list,
                metadata={
                    "name": "namedElement",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )

    @dataclass(kw_only=True)
    class ProportionalElection:
        is_election_result_complete: bool = field(
            metadata={
                "name": "isElectionResultComplete",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            }
        )
        list_value: list[ElectedType.ProportionalElection.List] = field(
            default_factory=list,
            metadata={
                "name": "list",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_occurs": 1,
            },
        )

        @dataclass(kw_only=True)
        class List:
            list_identification: str = field(
                metadata={
                    "name": "listIdentification",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                    "min_length": 1,
                    "max_length": 50,
                }
            )
            list_indenture_number: None | str = field(
                default=None,
                metadata={
                    "name": "listIndentureNumber",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                    "min_length": 1,
                    "max_length": 6,
                },
            )
            elected_candidate: list[
                ElectedType.ProportionalElection.List.ElectedCandidate
            ] = field(
                default_factory=list,
                metadata={
                    "name": "electedCandidate",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )
            count_of_seats_gained: int = field(
                metadata={
                    "name": "countOfSeatsGained",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                    "min_inclusive": 0,
                    "max_inclusive": 9999999,
                }
            )
            named_element: list[NamedElementType] = field(
                default_factory=list,
                metadata={
                    "name": "namedElement",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )

            @dataclass(kw_only=True)
            class ElectedCandidate:
                candidate_identification: str = field(
                    metadata={
                        "name": "candidateIdentification",
                        "type": "Element",
                        "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                        "min_length": 1,
                        "max_length": 50,
                    }
                )
                candidate_reference_on_position: list[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "candidateReferenceOnPosition",
                        "type": "Element",
                        "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                        "min_length": 1,
                        "max_length": 10,
                    },
                )
                is_elected_by_draw: None | bool = field(
                    default=None,
                    metadata={
                        "name": "isElectedByDraw",
                        "type": "Element",
                        "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                    },
                )
                mandate_type: None | MandateTypeType = field(
                    default=None,
                    metadata={
                        "name": "mandateType",
                        "type": "Element",
                        "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                    },
                )
                sort_id: None | int = field(
                    default=None,
                    metadata={
                        "name": "sortID",
                        "type": "Element",
                        "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                    },
                )
                named_element: list[NamedElementType] = field(
                    default_factory=list,
                    metadata={
                        "name": "namedElement",
                        "type": "Element",
                        "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                    },
                )


@dataclass(kw_only=True)
class ElectionGroupInfoType:
    class Meta:
        name = "electionGroupInfoType"

    election_group: ElectionGroupInfoType.ElectionGroup = field(
        metadata={
            "name": "electionGroup",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        }
    )
    counting_circle: list[CountingCircleType] = field(
        default_factory=list,
        metadata={
            "name": "countingCircle",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_occurs": 1,
        },
    )
    named_element: list[NamedElementType] = field(
        default_factory=list,
        metadata={
            "name": "namedElement",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )

    @dataclass(kw_only=True)
    class ElectionGroup:
        election_group_identification: None | str = field(
            default=None,
            metadata={
                "name": "electionGroupIdentification",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_length": 1,
                "max_length": 50,
            },
        )
        domain_of_influence: DomainOfInfluenceType = field(
            metadata={
                "name": "domainOfInfluence",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            }
        )
        superior_authority: None | DomainOfInfluenceType = field(
            default=None,
            metadata={
                "name": "superiorAuthority",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )
        election_group_position: None | int = field(
            default=None,
            metadata={
                "name": "electionGroupPosition",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )
        election_information: list[
            ElectionGroupInfoType.ElectionGroup.ElectionInformation
        ] = field(
            default_factory=list,
            metadata={
                "name": "electionInformation",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_occurs": 1,
            },
        )
        named_element: list[NamedElementType] = field(
            default_factory=list,
            metadata={
                "name": "namedElement",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )

        @dataclass(kw_only=True)
        class ElectionInformation:
            election: ElectionType = field(
                metadata={
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                }
            )
            other_identification: list[NamedIdType] = field(
                default_factory=list,
                metadata={
                    "name": "otherIdentification",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )
            quorum: None | Decimal = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                    "min_inclusive": Decimal("0.00"),
                    "max_inclusive": Decimal("100.00"),
                    "total_digits": 5,
                    "fraction_digits": 2,
                },
            )
            referenced_election_association_id: None | str = field(
                default=None,
                metadata={
                    "name": "referencedElectionAssociationId",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                    "min_length": 1,
                    "max_length": 50,
                },
            )
            candidate: list[CandidateType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )
            list_value: list[ListType] = field(
                default_factory=list,
                metadata={
                    "name": "list",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )
            list_union: list[ListUnionType] = field(
                default_factory=list,
                metadata={
                    "name": "listUnion",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )
            named_element: list[NamedElementType] = field(
                default_factory=list,
                metadata={
                    "name": "namedElement",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )


@dataclass(kw_only=True)
class ResultDataType:
    class Meta:
        name = "resultDataType"

    count_of_voters_information: CountOfVotersInformationType = field(
        metadata={
            "name": "countOfVotersInformation",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        }
    )
    voting_card_information: None | VotingCardInformationType = field(
        default=None,
        metadata={
            "name": "votingCardInformation",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )
    is_fully_counted: bool = field(
        metadata={
            "name": "isFullyCounted",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        }
    )
    released_timestamp: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "releasedTimestamp",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )
    lockout_timestamp: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "lockoutTimestamp",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )
    voter_turnout: None | Decimal = field(
        default=None,
        metadata={
            "name": "voterTurnout",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("100.00"),
            "total_digits": 5,
            "fraction_digits": 2,
        },
    )
    received_votes: int = field(
        metadata={
            "name": "receivedVotes",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        }
    )
    received_invalid_votes: int = field(
        metadata={
            "name": "receivedInvalidVotes",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        }
    )
    received_blank_votes: int = field(
        metadata={
            "name": "receivedBlankVotes",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        }
    )
    received_valid_votes: int = field(
        metadata={
            "name": "receivedValidVotes",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        }
    )
    count_of_yes_votes: int = field(
        metadata={
            "name": "countOfYesVotes",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        }
    )
    count_of_no_votes: int = field(
        metadata={
            "name": "countOfNoVotes",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        }
    )
    count_of_votes_without_answer: None | int = field(
        default=None,
        metadata={
            "name": "countOfVotesWithoutAnswer",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 9999999,
        },
    )
    named_element: list[NamedElementType] = field(
        default_factory=list,
        metadata={
            "name": "namedElement",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )


@dataclass(kw_only=True)
class CountingCircleInfoType:
    class Meta:
        name = "countingCircleInfoType"

    counting_circle: CountingCircleType = field(
        metadata={
            "name": "countingCircle",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        }
    )
    result_data: None | ResultDataType = field(
        default=None,
        metadata={
            "name": "resultData",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )


@dataclass(kw_only=True)
class ElectionResultType:
    class Meta:
        name = "electionResultType"

    election_identification: str = field(
        metadata={
            "name": "electionIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_length": 1,
            "max_length": 50,
        }
    )
    majority_election: None | ElectionResultType.MajorityElection = field(
        default=None,
        metadata={
            "name": "majorityElection",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )
    proportional_election: None | ElectionResultType.ProportionalElection = (
        field(
            default=None,
            metadata={
                "name": "proportionalElection",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )
    )
    named_element: list[NamedElementType] = field(
        default_factory=list,
        metadata={
            "name": "namedElement",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )

    @dataclass(kw_only=True)
    class MajorityElection:
        """
        :ivar candidate_result: The element is always delivered for all
            candidates that are known at the current time. All elements
            in candidate must therefore be contained in candidateResult.
            Addidional write-in candidates must be added in the
            structure, at the time they are known
        :ivar count_of_invalid_votes_total:
        :ivar count_of_blank_votes_total:
        :ivar count_of_individual_votes_total:
        :ivar named_element:
        """

        candidate_result: list[CandidateResultType] = field(
            default_factory=list,
            metadata={
                "name": "candidateResult",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )
        count_of_invalid_votes_total: int = field(
            metadata={
                "name": "countOfInvalidVotesTotal",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_inclusive": 0,
                "max_inclusive": 9999999,
            }
        )
        count_of_blank_votes_total: int = field(
            metadata={
                "name": "countOfBlankVotesTotal",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_inclusive": 0,
                "max_inclusive": 9999999,
            }
        )
        count_of_individual_votes_total: int = field(
            metadata={
                "name": "countOfIndividualVotesTotal",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_inclusive": 0,
                "max_inclusive": 9999999,
            }
        )
        named_element: list[NamedElementType] = field(
            default_factory=list,
            metadata={
                "name": "namedElement",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )

    @dataclass(kw_only=True)
    class ProportionalElection:
        count_of_changed_ballots_without_list_designation: int = field(
            metadata={
                "name": "countOfChangedBallotsWithoutListDesignation",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_inclusive": 0,
                "max_inclusive": 9999999,
            }
        )
        count_of_blank_votes_of_changed_ballots_without_list_designation: int = field(
            metadata={
                "name": "countOfBlankVotesOfChangedBallotsWithoutListDesignation",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_inclusive": 0,
                "max_inclusive": 9999999,
            }
        )
        list_results: list[ListResultType] = field(
            default_factory=list,
            metadata={
                "name": "listResults",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_occurs": 1,
            },
        )
        named_element: list[NamedElementType] = field(
            default_factory=list,
            metadata={
                "name": "namedElement",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )


@dataclass(kw_only=True)
class EventElectionInformationDeliveryType:
    """
    :ivar canton_id:
    :ivar polling_day:
    :ivar election_association:
    :ivar election_group_info: The electionGroup is always used, if
        there is an election. If it is not required to group several
        elections, it only contains a single election.
    :ivar number_of_entries:
    :ivar extension:
    """

    class Meta:
        name = "eventElectionInformationDeliveryType"

    canton_id: int = field(
        metadata={
            "name": "cantonId",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 1,
            "max_inclusive": 26,
        }
    )
    polling_day: XmlDate = field(
        metadata={
            "name": "pollingDay",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        }
    )
    election_association: list[ElectionAssociationType] = field(
        default_factory=list,
        metadata={
            "name": "electionAssociation",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )
    election_group_info: list[ElectionGroupInfoType] = field(
        default_factory=list,
        metadata={
            "name": "electionGroupInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )
    number_of_entries: int = field(
        metadata={
            "name": "numberOfEntries",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 999,
        }
    )
    extension: None | ExtensionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )


@dataclass(kw_only=True)
class CountingCircleResultType:
    class Meta:
        name = "countingCircleResultType"

    counting_circle: CountingCircleType = field(
        metadata={
            "name": "countingCircle",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        }
    )
    result_data: None | CountingCircleResultType.ResultData = field(
        default=None,
        metadata={
            "name": "resultData",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )

    @dataclass(kw_only=True)
    class ResultData:
        count_of_voters_information: CountOfVotersInformationType = field(
            metadata={
                "name": "countOfVotersInformation",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            }
        )
        voting_card_information: None | VotingCardInformationType = field(
            default=None,
            metadata={
                "name": "votingCardInformation",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )
        is_fully_counted: bool = field(
            metadata={
                "name": "isFullyCounted",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            }
        )
        released_timestamp: None | XmlDateTime = field(
            default=None,
            metadata={
                "name": "releasedTimestamp",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )
        lockout_timestamp: None | XmlDateTime = field(
            default=None,
            metadata={
                "name": "lockoutTimestamp",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )
        voter_turnout: None | Decimal = field(
            default=None,
            metadata={
                "name": "voterTurnout",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_inclusive": Decimal("0.00"),
                "max_inclusive": Decimal("100.00"),
                "total_digits": 5,
                "fraction_digits": 2,
            },
        )
        count_of_received_ballots: int = field(
            metadata={
                "name": "countOfReceivedBallots",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_inclusive": 0,
                "max_inclusive": 9999999,
            }
        )
        count_of_blank_ballots: int = field(
            metadata={
                "name": "countOfBlankBallots",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_inclusive": 0,
                "max_inclusive": 9999999,
            }
        )
        count_of_invalid_ballots: int = field(
            metadata={
                "name": "countOfInvalidBallots",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_inclusive": 0,
                "max_inclusive": 9999999,
            }
        )
        count_of_valid_ballots: int = field(
            metadata={
                "name": "countOfValidBallots",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_inclusive": 0,
                "max_inclusive": 9999999,
            }
        )
        election_result: ElectionResultType = field(
            metadata={
                "name": "electionResult",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            }
        )
        named_element: list[NamedElementType] = field(
            default_factory=list,
            metadata={
                "name": "namedElement",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )


@dataclass(kw_only=True)
class VoteInfoType:
    class Meta:
        name = "voteInfoType"

    vote: VoteType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        }
    )
    counting_circle_info: list[CountingCircleInfoType] = field(
        default_factory=list,
        metadata={
            "name": "countingCircleInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_occurs": 1,
        },
    )
    vote_result_data: None | VoteResultDataType = field(
        default=None,
        metadata={
            "name": "voteResultData",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )


@dataclass(kw_only=True)
class EventElectionResultDeliveryType:
    class Meta:
        name = "eventElectionResultDeliveryType"

    canton_id: int = field(
        metadata={
            "name": "cantonId",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 1,
            "max_inclusive": 26,
        }
    )
    polling_day: XmlDate = field(
        metadata={
            "name": "pollingDay",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        }
    )
    election_group_result: list[
        EventElectionResultDeliveryType.ElectionGroupResult
    ] = field(
        default_factory=list,
        metadata={
            "name": "electionGroupResult",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_occurs": 1,
        },
    )
    number_of_entries: int = field(
        metadata={
            "name": "numberOfEntries",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 999,
        }
    )
    extension: None | ExtensionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )

    @dataclass(kw_only=True)
    class ElectionGroupResult:
        election_group_identification: None | str = field(
            default=None,
            metadata={
                "name": "electionGroupIdentification",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_length": 1,
                "max_length": 50,
            },
        )
        election_result: list[
            EventElectionResultDeliveryType.ElectionGroupResult.ElectionResult
        ] = field(
            default_factory=list,
            metadata={
                "name": "electionResult",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                "min_occurs": 1,
            },
        )
        named_element: list[NamedElementType] = field(
            default_factory=list,
            metadata={
                "name": "namedElement",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            },
        )

        @dataclass(kw_only=True)
        class ElectionResult:
            election_identification: str = field(
                metadata={
                    "name": "electionIdentification",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                    "min_length": 1,
                    "max_length": 50,
                }
            )
            other_identification: list[NamedIdType] = field(
                default_factory=list,
                metadata={
                    "name": "otherIdentification",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )
            counting_circle_result: list[CountingCircleResultType] = field(
                default_factory=list,
                metadata={
                    "name": "countingCircleResult",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                    "min_occurs": 1,
                },
            )
            elected: None | ElectedType = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )
            draw_election: None | DrawElectionType = field(
                default=None,
                metadata={
                    "name": "drawElection",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )
            named_element: list[NamedElementType] = field(
                default_factory=list,
                metadata={
                    "name": "namedElement",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
                },
            )


@dataclass(kw_only=True)
class EventVoteBaseDeliveryType:
    class Meta:
        name = "eventVoteBaseDeliveryType"

    canton_id: int = field(
        metadata={
            "name": "cantonId",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 1,
            "max_inclusive": 26,
        }
    )
    polling_day: XmlDate = field(
        metadata={
            "name": "pollingDay",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        }
    )
    vote_info: list[VoteInfoType] = field(
        default_factory=list,
        metadata={
            "name": "voteInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )
    number_of_entries: int = field(
        metadata={
            "name": "numberOfEntries",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
            "min_inclusive": 0,
            "max_inclusive": 999,
        }
    )
    extension: None | ExtensionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0252/2",
        },
    )


@dataclass(kw_only=True)
class Delivery:
    class Meta:
        name = "delivery"
        namespace = "http://www.ech.ch/xmlns/eCH-0252/2"

    delivery_header: HeaderType = field(
        metadata={
            "name": "deliveryHeader",
            "type": "Element",
        }
    )
    vote_base_delivery: None | EventVoteBaseDeliveryType = field(
        default=None,
        metadata={
            "name": "voteBaseDelivery",
            "type": "Element",
        },
    )
    election_information_delivery: (
        None | EventElectionInformationDeliveryType
    ) = field(
        default=None,
        metadata={
            "name": "electionInformationDelivery",
            "type": "Element",
        },
    )
    election_result_delivery: None | EventElectionResultDeliveryType = field(
        default=None,
        metadata={
            "name": "electionResultDelivery",
            "type": "Element",
        },
    )
