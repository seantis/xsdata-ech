from pytest import fixture
from typing import Iterator
from xsdata_ech.e_ch_0058_5_0 import Header
from xsdata_ech.e_ch_0252_2_0 import (
    CandidateOrWriteInCandidateType,
    CandidateResultType,
    CountingCircleResultType,
    CountingCircleType,
    CountOfVotersInformationType,
    Delivery,
    ElectionResultType,
    ElectedType,
    EventElectionResultDeliveryType,
    VoterTypeType
)
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDate

SubtotalInfo = CountOfVotersInformationType.SubtotalInfo
ElectionGroupResult = EventElectionResultDeliveryType.ElectionGroupResult
ElectionResult = ElectionGroupResult.ElectionResult
MajorityElectionResult = ElectionResultType.MajorityElection
MajorityElectionElected = ElectedType.MajorityElection
ElectedCandidate = MajorityElectionElected.ElectedCandidate
ResultData = CountingCircleResultType.ResultData


@fixture()
def delivery() -> Iterator[Delivery]:
    counting_circle_result = [
        CountingCircleResultType(
            counting_circle=CountingCircleType(
                counting_circle_id='3901',
            ),
            result_data=ResultData(
                count_of_voters_information=(
                    CountOfVotersInformationType(
                        count_of_voters_total=100,
                        subtotal_info=[
                            SubtotalInfo(
                                count_of_voters=100,
                                voter_type=(
                                    VoterTypeType.VALUE_2
                                ),
                            )
                        ]
                    )
                ),
                is_fully_counted=True,
                count_of_received_ballots=100,
                count_of_blank_ballots=1,
                count_of_invalid_ballots=2,
                count_of_valid_ballots=97,
                election_result=ElectionResultType(
                    election_identification='election-id',
                    majority_election=MajorityElectionResult(
                        candidate_result=[
                            CandidateResultType(
                                candidate_or_write_in_candidate=(
                                    CandidateOrWriteInCandidateType(
                                        candidate_identification=(
                                            'candidate-id'
                                        ),
                                    )
                                ),
                                count_of_votes_total=10
                            )
                        ],
                        count_of_invalid_votes_total=0,
                        count_of_blank_votes_total=0,
                        count_of_individual_votes_total=0
                    )
                )
            )
        )
    ]

    elected = ElectedType(
        majority_election=MajorityElectionElected(
            absolute_majority=500,
            is_election_result_complete=True,
            elected_candidate=[
                ElectedCandidate(
                    candidate_or_write_in_candidate=(
                        CandidateOrWriteInCandidateType(
                            candidate_identification='candidate-id'
                        )
                    ),
                )
            ]
        )
    )

    yield Delivery(
        delivery_header=Header(),
        election_result_delivery=EventElectionResultDeliveryType(
            canton_id=1,
            polling_day=XmlDate(2023, 1, 1),
            number_of_entries=1,
            election_group_result=[
                ElectionGroupResult(
                    election_group_identification='group-id',
                    election_result=[
                        ElectionResult(
                            election_identification='election-id',
                            counting_circle_result=counting_circle_result,
                            elected=elected
                        )
                    ]
                )
            ]

        )
    )


def test_ech_0252_majorz_election_result_xml(delivery: Delivery) -> None:
    # to xml
    config = SerializerConfig(pretty_print=True)
    serializer = XmlSerializer(config=config)
    xml = serializer.render(delivery)

    # from xml
    parser = XmlParser(context=XmlContext())
    parsed: Delivery = parser.from_string(xml)
    assert delivery == parsed


