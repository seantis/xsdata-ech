from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime

from xsdata_ech.e_ch_0006_2_0 import ResidencePermitType
from xsdata_ech.e_ch_0008_3_0 import CountryType
from xsdata_ech.e_ch_0010_6_0 import (
    AddressInformationType,
    MrMrsType,
    PersonMailAddressType,
    SwissAddressInformationType,
)
from xsdata_ech.e_ch_0044_4_1 import (
    DatePartiallyKnownType,
    NamedPersonIdType,
    SexType,
)

__NAMESPACE__ = "http://www.ech.ch/xmlns/eCH-0155/5"


@dataclass(kw_only=True)
class AnswerOptionIdentificationType:
    class Meta:
        name = "answerOptionIdentificationType"

    answer_identification: str = field(
        metadata={
            "name": "answerIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        }
    )
    answer_sequence_number: int = field(
        metadata={
            "name": "answerSequenceNumber",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )
    answer_text_information: list[
        AnswerOptionIdentificationType.AnswerTextInformation
    ] = field(
        default_factory=list,
        metadata={
            "name": "answerTextInformation",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class AnswerTextInformation:
        language: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "length": 2,
            }
        )
        answer_text_short: None | str = field(
            default=None,
            metadata={
                "name": "answerTextShort",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 10,
            },
        )
        answer_text: str = field(
            metadata={
                "name": "answerText",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 30,
            }
        )


class AnswerTypeType(Enum):
    """
    Two answer options (answerOptionIdentificationType) must be provided
    with answerType 8.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8


@dataclass(kw_only=True)
class CandidateGroupDescriptionInformationType:
    class Meta:
        name = "candidateGroupDescriptionInformationType"

    candidate_group_description_info: list[
        CandidateGroupDescriptionInformationType.CandidateGroupDescriptionInfo
    ] = field(
        default_factory=list,
        metadata={
            "name": "candidateGroupDescriptionInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class CandidateGroupDescriptionInfo:
        language: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "length": 2,
            }
        )
        candidate_group_description_short: None | str = field(
            default=None,
            metadata={
                "name": "candidateGroupDescriptionShort",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 20,
            },
        )
        candidate_group_description: str = field(
            metadata={
                "name": "candidateGroupDescription",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 100,
            }
        )


@dataclass(kw_only=True)
class CandidateTextInformationType:
    class Meta:
        name = "candidateTextInformationType"

    candidate_text_info: list[
        CandidateTextInformationType.CandidateTextInfo
    ] = field(
        default_factory=list,
        metadata={
            "name": "candidateTextInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class CandidateTextInfo:
        language: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "length": 2,
            }
        )
        candidate_text: str = field(
            metadata={
                "name": "candidateText",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 500,
            }
        )


@dataclass(kw_only=True)
class ContestDescriptionInformationType:
    class Meta:
        name = "contestDescriptionInformationType"

    contest_description_info: list[
        ContestDescriptionInformationType.ContestDescriptionInfo
    ] = field(
        default_factory=list,
        metadata={
            "name": "contestDescriptionInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class ContestDescriptionInfo:
        language: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "length": 2,
            }
        )
        contest_description: str = field(
            metadata={
                "name": "contestDescription",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 100,
            }
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
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        },
    )
    counting_circle_name: None | str = field(
        default=None,
        metadata={
            "name": "countingCircleName",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 100,
        },
    )


class DomainOfInfluenceTypeType(Enum):
    CH = "CH"
    CT = "CT"
    BZ = "BZ"
    MU = "MU"
    SC = "SC"
    KI = "KI"
    OG = "OG"
    KO = "KO"
    SK = "SK"
    GT = "GT"
    AN = "AN"


@dataclass(kw_only=True)
class EVotingPeriodType:
    class Meta:
        name = "eVotingPeriodType"

    e_voting_period_from: XmlDateTime = field(
        metadata={
            "name": "eVotingPeriodFrom",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )
    e_voting_period_till: XmlDateTime = field(
        metadata={
            "name": "eVotingPeriodTill",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )


@dataclass(kw_only=True)
class ElectionDescriptionInformationType:
    class Meta:
        name = "electionDescriptionInformationType"

    election_description_info: list[
        ElectionDescriptionInformationType.ElectionDescriptionInfo
    ] = field(
        default_factory=list,
        metadata={
            "name": "electionDescriptionInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class ElectionDescriptionInfo:
        language: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "length": 2,
            }
        )
        election_description_short: None | str = field(
            default=None,
            metadata={
                "name": "electionDescriptionShort",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 100,
            },
        )
        election_description: str = field(
            metadata={
                "name": "electionDescription",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 255,
            }
        )


class ElectionRelationType(Enum):
    VALUE_1 = 1
    VALUE_2 = 2


@dataclass(kw_only=True)
class ElectronicBallotDescriptionInformationType:
    class Meta:
        name = "electronicBallotDescriptionInformationType"

    electronic_ballot_description_info: list[
        "ElectronicBallotDescriptionInformationType"
        ".ElectronicBallotDescriptionInfo"
    ] = field(
        default_factory=list,
        metadata={
            "name": "electronicBallotDescriptionInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class ElectronicBallotDescriptionInfo:
        language: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "length": 2,
            }
        )
        electronic_ballot_description_long: None | str = field(
            default=None,
            metadata={
                "name": "electronicBallotDescriptionLong",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 700,
            },
        )
        electronic_ballot_description_short: None | str = field(
            default=None,
            metadata={
                "name": "electronicBallotDescriptionShort",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 255,
            },
        )


@dataclass(kw_only=True)
class ElectronicBallotQuestionType:
    class Meta:
        name = "electronicBallotQuestionType"

    electronic_ballot_question_info: list[
        ElectronicBallotQuestionType.ElectronicBallotQuestionInfo
    ] = field(
        default_factory=list,
        metadata={
            "name": "electronicBallotQuestionInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class ElectronicBallotQuestionInfo:
        language: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "length": 2,
            }
        )
        electronic_ballot_question_title: None | str = field(
            default=None,
            metadata={
                "name": "electronicBallotQuestionTitle",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 100,
            },
        )
        electronic_ballot_question: str = field(
            metadata={
                "name": "electronicBallotQuestion",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 700,
            }
        )


class EligibilityType(Enum):
    IMPLICITLY_ELIGIBLE = "implicitly eligible"
    EXPLICITLY_REPORTED = "explicitly reported"


@dataclass(kw_only=True)
class ExtensionType:
    class Meta:
        name = "extensionType"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ListDescriptionInformationType:
    class Meta:
        name = "listDescriptionInformationType"

    list_description_info: list[
        ListDescriptionInformationType.ListDescriptionInfo
    ] = field(
        default_factory=list,
        metadata={
            "name": "listDescriptionInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class ListDescriptionInfo:
        language: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "length": 2,
            }
        )
        list_description_short: None | str = field(
            default=None,
            metadata={
                "name": "listDescriptionShort",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 20,
            },
        )
        list_description: str = field(
            metadata={
                "name": "listDescription",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 100,
            }
        )


class ListRelationType(Enum):
    VALUE_1 = 1
    VALUE_2 = 2


@dataclass(kw_only=True)
class ListUnionBallotTextType:
    class Meta:
        name = "listUnionBallotTextType"

    list_union_ballot_text_info: list[
        ListUnionBallotTextType.ListUnionBallotTextInfo
    ] = field(
        default_factory=list,
        metadata={
            "name": "listUnionBallotTextInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class ListUnionBallotTextInfo:
        language: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "length": 2,
            }
        )
        list_union_ballot_text: str = field(
            metadata={
                "name": "listUnionBallotText",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 500,
            }
        )


@dataclass(kw_only=True)
class ListUnionDescriptionType:
    class Meta:
        name = "listUnionDescriptionType"

    list_union_description_info: list[
        ListUnionDescriptionType.ListUnionDescriptionInfo
    ] = field(
        default_factory=list,
        metadata={
            "name": "listUnionDescriptionInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class ListUnionDescriptionInfo:
        language: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "length": 2,
            }
        )
        list_union_description: str = field(
            metadata={
                "name": "listUnionDescription",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 255,
            }
        )


@dataclass(kw_only=True)
class OccupationalTitleInformationType:
    class Meta:
        name = "occupationalTitleInformationType"

    occupational_title_info: list[
        OccupationalTitleInformationType.OccupationalTitleInfo
    ] = field(
        default_factory=list,
        metadata={
            "name": "occupationalTitleInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class OccupationalTitleInfo:
        language: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "length": 2,
            }
        )
        occupational_title: str = field(
            metadata={
                "name": "occupationalTitle",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 250,
            }
        )


@dataclass(kw_only=True)
class OtherIdentificationType:
    class Meta:
        name = "otherIdentificationType"

    id_name: str = field(
        metadata={
            "name": "idName",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 20,
        }
    )
    id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        }
    )


@dataclass(kw_only=True)
class PartyAffiliationInformationType:
    class Meta:
        name = "partyAffiliationInformationType"

    party_affiliation_info: list[
        PartyAffiliationInformationType.PartyAffiliationInfo
    ] = field(
        default_factory=list,
        metadata={
            "name": "partyAffiliationInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class PartyAffiliationInfo:
        language: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "length": 2,
            }
        )
        party_affiliation_short: str = field(
            metadata={
                "name": "partyAffiliationShort",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 12,
            }
        )
        party_affiliation_long: None | str = field(
            default=None,
            metadata={
                "name": "partyAffiliationLong",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 100,
            },
        )


@dataclass(kw_only=True)
class RoleInformationType:
    class Meta:
        name = "roleInformationType"

    role_info: list[RoleInformationType.RoleInfo] = field(
        default_factory=list,
        metadata={
            "name": "roleInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class RoleInfo:
        language: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "length": 2,
            }
        )
        role: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 100,
            }
        )


@dataclass(kw_only=True)
class TieBreakQuestionType:
    class Meta:
        name = "tieBreakQuestionType"

    tie_break_question_info: list[
        TieBreakQuestionType.TieBreakQuestionInfo
    ] = field(
        default_factory=list,
        metadata={
            "name": "tieBreakQuestionInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class TieBreakQuestionInfo:
        language: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "length": 2,
            }
        )
        tie_break_question_title: None | str = field(
            default=None,
            metadata={
                "name": "tieBreakQuestionTitle",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 100,
            },
        )
        tie_break_question: str = field(
            metadata={
                "name": "tieBreakQuestion",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 700,
            }
        )
        tie_break_question2: None | str = field(
            default=None,
            metadata={
                "name": "tieBreakQuestion2",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 700,
            },
        )


class TypeOfElectionType(Enum):
    VALUE_1 = 1
    VALUE_2 = 2


@dataclass(kw_only=True)
class VoteDescriptionInformationType:
    class Meta:
        name = "voteDescriptionInformationType"

    vote_description_info: list[
        VoteDescriptionInformationType.VoteDescriptionInfo
    ] = field(
        default_factory=list,
        metadata={
            "name": "voteDescriptionInfo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class VoteDescriptionInfo:
        language: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "length": 2,
            }
        )
        vote_description: str = field(
            metadata={
                "name": "voteDescription",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 100,
            }
        )


class VoterTypeType(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class VotingChannelType(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


@dataclass(kw_only=True)
class AnswerInformationType:
    class Meta:
        name = "answerInformationType"

    answer_type: None | AnswerTypeType = field(
        default=None,
        metadata={
            "name": "answerType",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    answer_option_identification: list[AnswerOptionIdentificationType] = field(
        default_factory=list,
        metadata={
            "name": "answerOptionIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )


@dataclass(kw_only=True)
class CandidateGroupType:
    class Meta:
        name = "candidateGroupType"

    candidate_group_identification: str = field(
        metadata={
            "name": "candidateGroupIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        }
    )
    sort_id: None | int = field(
        default=None,
        metadata={
            "name": "sortID",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    candidate_group_description: CandidateGroupDescriptionInformationType = (
        field(
            metadata={
                "name": "candidateGroupDescription",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            }
        )
    )


@dataclass(kw_only=True)
class CandidatePositionInformationType:
    class Meta:
        name = "candidatePositionInformationType"

    position_on_list: int = field(
        metadata={
            "name": "positionOnList",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )
    candidate_reference_on_position: str = field(
        metadata={
            "name": "candidateReferenceOnPosition",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 10,
        }
    )
    candidate_identification: str = field(
        metadata={
            "name": "candidateIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        }
    )
    candidate_text_on_position: CandidateTextInformationType = field(
        metadata={
            "name": "candidateTextOnPosition",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )
    checking_number: None | str = field(
        default=None,
        metadata={
            "name": "checkingNumber",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )


@dataclass(kw_only=True)
class ContestType:
    class Meta:
        name = "contestType"

    contest_identification: str = field(
        metadata={
            "name": "contestIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        }
    )
    contest_date: XmlDate = field(
        metadata={
            "name": "contestDate",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )
    contest_description: None | ContestDescriptionInformationType = field(
        default=None,
        metadata={
            "name": "contestDescription",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    e_voting_period: None | EVotingPeriodType = field(
        default=None,
        metadata={
            "name": "eVotingPeriod",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )


@dataclass(kw_only=True)
class CountingCircle(CountingCircleType):
    class Meta:
        name = "countingCircle"
        namespace = "http://www.ech.ch/xmlns/eCH-0155/5"


@dataclass(kw_only=True)
class DomainOfInfluenceType:
    class Meta:
        name = "domainOfInfluenceType"

    domain_of_influence_type: DomainOfInfluenceTypeType = field(
        metadata={
            "name": "domainOfInfluenceType",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )
    domain_of_influence_identification: str = field(
        metadata={
            "name": "domainOfInfluenceIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        }
    )
    domain_of_influence_name: str = field(
        metadata={
            "name": "domainOfInfluenceName",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 100,
        }
    )
    domain_of_influence_shortname: None | str = field(
        default=None,
        metadata={
            "name": "domainOfInfluenceShortname",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 5,
        },
    )


@dataclass(kw_only=True)
class ElectionGroupDescriptionType(ElectionDescriptionInformationType):
    class Meta:
        name = "electionGroupDescriptionType"


@dataclass(kw_only=True)
class ListUnionType:
    class Meta:
        name = "listUnionType"

    list_union_identification: str = field(
        metadata={
            "name": "listUnionIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        }
    )
    list_union_description: ListUnionDescriptionType = field(
        metadata={
            "name": "listUnionDescription",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )
    list_union_type: ListRelationType = field(
        metadata={
            "name": "listUnionType",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )
    referenced_list: list[str] = field(
        default_factory=list,
        metadata={
            "name": "referencedList",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 50,
        },
    )
    referenced_list_union: None | str = field(
        default=None,
        metadata={
            "name": "referencedListUnion",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        },
    )


@dataclass(kw_only=True)
class PoliticalAddressInfoType:
    class Meta:
        name = "politicalAddressInfoType"

    political_address: SwissAddressInformationType = field(
        metadata={
            "name": "politicalAddress",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )
    municipality_id: int = field(
        metadata={
            "name": "municipalityId",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_inclusive": 1,
            "max_inclusive": 9999,
            "total_digits": 4,
        }
    )


@dataclass(kw_only=True)
class ReferencedElectionInformationType:
    class Meta:
        name = "referencedElectionInformationType"

    referenced_election: str = field(
        metadata={
            "name": "referencedElection",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        }
    )
    election_relation: ElectionRelationType = field(
        metadata={
            "name": "electionRelation",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )


@dataclass(kw_only=True)
class VotingPersonIdentificationType:
    class Meta:
        name = "votingPersonIdentificationType"

    vn: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_inclusive": 7560000000001,
            "max_inclusive": 7569999999999,
        },
    )
    local_person_id: NamedPersonIdType = field(
        metadata={
            "name": "localPersonId",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )
    other_person_id: list[NamedPersonIdType] = field(
        default_factory=list,
        metadata={
            "name": "otherPersonId",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    official_name: None | str = field(
        default=None,
        metadata={
            "name": "officialName",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 100,
        },
    )
    first_name: None | str = field(
        default=None,
        metadata={
            "name": "firstName",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 100,
        },
    )
    sex: None | SexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    date_of_birth: None | DatePartiallyKnownType = field(
        default=None,
        metadata={
            "name": "dateOfBirth",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )


@dataclass(kw_only=True)
class CandidateGroup(CandidateGroupType):
    class Meta:
        name = "candidateGroup"
        namespace = "http://www.ech.ch/xmlns/eCH-0155/5"


@dataclass(kw_only=True)
class CandidateType:
    class Meta:
        name = "candidateType"

    vn: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_inclusive": 7560000000001,
            "max_inclusive": 7569999999999,
        },
    )
    candidate_identification: str = field(
        metadata={
            "name": "candidateIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        }
    )
    bf_snumber_canton: None | int = field(
        default=None,
        metadata={
            "name": "BfSNumberCanton",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_inclusive": 1,
            "max_inclusive": 26,
        },
    )
    family_name: None | str = field(
        default=None,
        metadata={
            "name": "familyName",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 100,
        },
    )
    first_name: None | str = field(
        default=None,
        metadata={
            "name": "firstName",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 100,
        },
    )
    political_family_name: None | str = field(
        default=None,
        metadata={
            "name": "politicalFamilyName",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 100,
        },
    )
    political_first_name: None | str = field(
        default=None,
        metadata={
            "name": "politicalFirstName",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 100,
        },
    )
    call_name: None | str = field(
        default=None,
        metadata={
            "name": "callName",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 100,
        },
    )
    candidate_text: None | CandidateTextInformationType = field(
        default=None,
        metadata={
            "name": "candidateText",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    date_of_birth: None | XmlDate = field(
        default=None,
        metadata={
            "name": "dateOfBirth",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    year_of_birth: None | XmlPeriod = field(
        default=None,
        metadata={
            "name": "yearOfBirth",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    sex: None | SexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    occupational_title: None | OccupationalTitleInformationType = field(
        default=None,
        metadata={
            "name": "occupationalTitle",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    contact_address: None | PersonMailAddressType = field(
        default=None,
        metadata={
            "name": "contactAddress",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    political_address: None | PoliticalAddressInfoType = field(
        default=None,
        metadata={
            "name": "politicalAddress",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    dwelling_address: None | AddressInformationType = field(
        default=None,
        metadata={
            "name": "dwellingAddress",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    swiss: None | CandidateType.Swiss = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    foreigner: None | CandidateType.Foreigner = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    mr_mrs: None | MrMrsType = field(
        default=None,
        metadata={
            "name": "mrMrs",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "max_length": 50,
        },
    )
    language_of_correspondence: None | str = field(
        default=None,
        metadata={
            "name": "languageOfCorrespondence",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "length": 2,
        },
    )
    incumbent_yes_no: None | bool = field(
        default=None,
        metadata={
            "name": "incumbentYesNo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    candidate_reference: None | str = field(
        default=None,
        metadata={
            "name": "candidateReference",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 10,
        },
    )
    role: None | RoleInformationType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    party_affiliation: None | PartyAffiliationInformationType = field(
        default=None,
        metadata={
            "name": "partyAffiliation",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    eligibility: None | EligibilityType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    sort_id: None | int = field(
        default=None,
        metadata={
            "name": "sortID",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    candidate_group_identification: list[str] = field(
        default_factory=list,
        metadata={
            "name": "candidateGroupIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        },
    )

    @dataclass(kw_only=True)
    class Swiss:
        origin: list[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 80,
            },
        )

    @dataclass(kw_only=True)
    class Foreigner:
        residence_permit: None | ResidencePermitType = field(
            metadata={
                "name": "residencePermit",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "nillable": True,
            }
        )
        dwelling_address: SwissAddressInformationType = field(
            metadata={
                "name": "dwellingAddress",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            }
        )
        in_canton_since: XmlDate = field(
            metadata={
                "name": "inCantonSince",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            }
        )
        nationality: CountryType = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            }
        )


@dataclass(kw_only=True)
class Contest(ContestType):
    class Meta:
        name = "contest"
        namespace = "http://www.ech.ch/xmlns/eCH-0155/5"


@dataclass(kw_only=True)
class DomainOfInfluence(DomainOfInfluenceType):
    class Meta:
        name = "domainOfInfluence"
        namespace = "http://www.ech.ch/xmlns/eCH-0155/5"


@dataclass(kw_only=True)
class ElectionType:
    class Meta:
        name = "electionType"

    election_identification: str = field(
        metadata={
            "name": "electionIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        }
    )
    other_identification: list[OtherIdentificationType] = field(
        default_factory=list,
        metadata={
            "name": "otherIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    type_of_election: TypeOfElectionType = field(
        metadata={
            "name": "typeOfElection",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )
    election_position: None | int = field(
        default=None,
        metadata={
            "name": "electionPosition",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    election_description: None | ElectionDescriptionInformationType = field(
        default=None,
        metadata={
            "name": "electionDescription",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    number_of_mandates: int = field(
        metadata={
            "name": "numberOfMandates",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )
    referenced_election: list[ReferencedElectionInformationType] = field(
        default_factory=list,
        metadata={
            "name": "referencedElection",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )


@dataclass(kw_only=True)
class ListType:
    class Meta:
        name = "listType"

    list_identification: str = field(
        metadata={
            "name": "listIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        }
    )
    list_indenture_number: str = field(
        metadata={
            "name": "listIndentureNumber",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 6,
        }
    )
    list_description: ListDescriptionInformationType = field(
        metadata={
            "name": "listDescription",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )
    is_empty_list: bool = field(
        metadata={
            "name": "isEmptyList",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )
    list_order_of_precedence: None | int = field(
        default=None,
        metadata={
            "name": "listOrderOfPrecedence",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    total_positions_on_list: None | int = field(
        default=None,
        metadata={
            "name": "totalPositionsOnList",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    candidate_position: list[CandidatePositionInformationType] = field(
        default_factory=list,
        metadata={
            "name": "candidatePosition",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    empty_list_positions: None | int = field(
        default=None,
        metadata={
            "name": "emptyListPositions",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    list_union_ballot_text: None | ListUnionBallotTextType = field(
        default=None,
        metadata={
            "name": "listUnionBallotText",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )


@dataclass(kw_only=True)
class QuestionInformationType:
    class Meta:
        name = "questionInformationType"

    question_identification: str = field(
        metadata={
            "name": "questionIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        }
    )
    electronic_ballot_question_number: None | str = field(
        default=None,
        metadata={
            "name": "electronicBallotQuestionNumber",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 15,
        },
    )
    question_position: None | int = field(
        default=None,
        metadata={
            "name": "questionPosition",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    answer_information: None | AnswerInformationType = field(
        default=None,
        metadata={
            "name": "answerInformation",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    electronic_ballot_question: ElectronicBallotQuestionType = field(
        metadata={
            "name": "electronicBallotQuestion",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )


@dataclass(kw_only=True)
class TieBreakInformationType:
    class Meta:
        name = "tieBreakInformationType"

    answer_information: None | AnswerInformationType = field(
        default=None,
        metadata={
            "name": "answerInformation",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    question_identification: str = field(
        metadata={
            "name": "questionIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        }
    )
    tie_break_question_number: None | str = field(
        default=None,
        metadata={
            "name": "tieBreakQuestionNumber",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 15,
        },
    )
    question_position: None | int = field(
        default=None,
        metadata={
            "name": "questionPosition",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    tie_break_question: TieBreakQuestionType = field(
        metadata={
            "name": "tieBreakQuestion",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )
    referenced_question1: None | str = field(
        default=None,
        metadata={
            "name": "referencedQuestion1",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        },
    )
    referenced_question2: None | str = field(
        default=None,
        metadata={
            "name": "referencedQuestion2",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
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
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        }
    )
    other_identification: list[OtherIdentificationType] = field(
        default_factory=list,
        metadata={
            "name": "otherIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    domain_of_influence: DomainOfInfluenceType = field(
        metadata={
            "name": "domainOfInfluence",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )
    vote_description: None | VoteDescriptionInformationType = field(
        default=None,
        metadata={
            "name": "voteDescription",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )


@dataclass(kw_only=True)
class VotingCardType:
    class Meta:
        name = "votingCardType"

    voting_card_number: None | str = field(
        default=None,
        metadata={
            "name": "votingCardNumber",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        },
    )
    voting_person_identification: None | VotingPersonIdentificationType = (
        field(
            default=None,
            metadata={
                "name": "votingPersonIdentification",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            },
        )
    )
    domain_of_influence: list[DomainOfInfluenceType] = field(
        default_factory=list,
        metadata={
            "name": "domainOfInfluence",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    voter_type: None | VoterTypeType = field(
        default=None,
        metadata={
            "name": "voterType",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    voting_channel: None | VotingChannelType = field(
        default=None,
        metadata={
            "name": "votingChannel",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    date_of_voting: None | XmlDate = field(
        default=None,
        metadata={
            "name": "dateOfVoting",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    time_of_voting: None | XmlTime = field(
        default=None,
        metadata={
            "name": "timeOfVoting",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    place_of_voting: None | str = field(
        default=None,
        metadata={
            "name": "placeOfVoting",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 100,
        },
    )
    electronic_voting_card_yes_no: None | bool = field(
        default=None,
        metadata={
            "name": "electronicVotingCardYesNo",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )


@dataclass(kw_only=True)
class Candidate(CandidateType):
    class Meta:
        name = "candidate"
        namespace = "http://www.ech.ch/xmlns/eCH-0155/5"


@dataclass(kw_only=True)
class Election(ElectionType):
    class Meta:
        name = "election"
        namespace = "http://www.ech.ch/xmlns/eCH-0155/5"


@dataclass(kw_only=True)
class ElectronicBallotType:
    class Meta:
        name = "electronicBallotType"

    electronic_ballot_identification: str = field(
        metadata={
            "name": "electronicBallotIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            "min_length": 1,
            "max_length": 50,
        }
    )
    other_identification: list[OtherIdentificationType] = field(
        default_factory=list,
        metadata={
            "name": "otherIdentification",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    electronic_ballot_position: int = field(
        metadata={
            "name": "electronicBallotPosition",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        }
    )
    electronic_ballot_description: (
        None | ElectronicBallotDescriptionInformationType
    ) = field(
        default=None,
        metadata={
            "name": "electronicBallotDescription",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    electronic_ballot_group: (
        None | ElectronicBallotDescriptionInformationType
    ) = field(
        default=None,
        metadata={
            "name": "electronicBallotGroup",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    standard_electronic_ballot: (
        None | ElectronicBallotType.StandardElectronicBallot
    ) = field(
        default=None,
        metadata={
            "name": "standardElectronicBallot",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    variant_electronic_ballot: (
        None | ElectronicBallotType.VariantElectronicBallot
    ) = field(
        default=None,
        metadata={
            "name": "variantElectronicBallot",
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )
    extension: None | ExtensionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
        },
    )

    @dataclass(kw_only=True)
    class StandardElectronicBallot:
        question_identification: str = field(
            metadata={
                "name": "questionIdentification",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 50,
            }
        )
        electronic_ballot_question_number: None | str = field(
            default=None,
            metadata={
                "name": "electronicBallotQuestionNumber",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_length": 1,
                "max_length": 15,
            },
        )
        answer_information: None | AnswerInformationType = field(
            default=None,
            metadata={
                "name": "answerInformation",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            },
        )
        electronic_ballot_question: ElectronicBallotQuestionType = field(
            metadata={
                "name": "electronicBallotQuestion",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            }
        )

    @dataclass(kw_only=True)
    class VariantElectronicBallot:
        question_information: list[
            ElectronicBallotType.VariantElectronicBallot.QuestionInformation
        ] = field(
            default_factory=list,
            metadata={
                "name": "questionInformation",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                "min_occurs": 2,
            },
        )
        tie_break_information: list[
            ElectronicBallotType.VariantElectronicBallot.TieBreakInformation
        ] = field(
            default_factory=list,
            metadata={
                "name": "tieBreakInformation",
                "type": "Element",
                "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
            },
        )

        @dataclass(kw_only=True)
        class QuestionInformation(QuestionInformationType):
            question_group_number: None | str = field(
                default=None,
                metadata={
                    "name": "questionGroupNumber",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                    "min_length": 1,
                    "max_length": 15,
                },
            )

        @dataclass(kw_only=True)
        class TieBreakInformation(TieBreakInformationType):
            question_group_number: None | str = field(
                default=None,
                metadata={
                    "name": "questionGroupNumber",
                    "type": "Element",
                    "namespace": "http://www.ech.ch/xmlns/eCH-0155/5",
                    "min_length": 1,
                    "max_length": 15,
                },
            )


@dataclass(kw_only=True)
class List(ListType):
    class Meta:
        name = "list"
        namespace = "http://www.ech.ch/xmlns/eCH-0155/5"


@dataclass(kw_only=True)
class Vote(VoteType):
    class Meta:
        name = "vote"
        namespace = "http://www.ech.ch/xmlns/eCH-0155/5"


@dataclass(kw_only=True)
class VotingCard(VotingCardType):
    class Meta:
        name = "votingCard"
        namespace = "http://www.ech.ch/xmlns/eCH-0155/5"


@dataclass(kw_only=True)
class ElectronicBallot(ElectronicBallotType):
    class Meta:
        name = "electronicBallot"
        namespace = "http://www.ech.ch/xmlns/eCH-0155/5"
