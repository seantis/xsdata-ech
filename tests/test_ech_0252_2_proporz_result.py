from pytest import fixture
from typing import Iterator
from xsdata_ech.e_ch_0058_5_0 import Header
from xsdata_ech.e_ch_0252_2_0 import (
    CandidateListResultType,
    CountingCircleResultType,
    CountingCircleType,
    CountOfVotersInformationType,
    Delivery,
    ElectionResultType,
    ElectedType,
    EventElectionResultDeliveryType,
    ListResultType,
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
ProportionalElectionResult = ElectionResultType.ProportionalElection
ProportionalElectionElected = ElectedType.ProportionalElection
ElectedCandidate = ProportionalElectionElected.List.ElectedCandidate
CandidateResults = ListResultType.CandidateResults
CandidateListResultsInfo = CandidateResults.CandidateListResultsInfo
ResultData = CountingCircleResultType.ResultData


@fixture()
def delivery() -> Iterator[Delivery]:
    candidate_list_results_info = CandidateListResultsInfo(
        candidate_list_results=[
            CandidateListResultType(
                list_identification='list-id',
                count_of_votes_from_changed_ballots=0
            )
        ],
        count_of_votes_from_ballots_without_list_designation=0,
    )
    proportional_election = ProportionalElectionResult(
        count_of_changed_ballots_without_list_designation=0,
        count_of_blank_votes_of_changed_ballots_without_list_designation=0,
        list_results=[
            ListResultType(
                list_identification='list-id',
                count_of_changed_ballots=0,
                count_of_unchanged_ballots=0,
                count_of_candidate_votes=0,
                count_of_additional_votes=0,
                candidate_results=[
                    CandidateResults(
                        candidate_identification='candidate-id',
                        count_of_votes_from_changed_ballots=0,
                        count_of_votes_from_unchanged_ballots=0,
                        candidate_list_results_info=candidate_list_results_info
                    )
                ]
            )
        ]
    )
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
                    proportional_election=proportional_election
                )
            )
        )
    ]

    # todo:
    elected = ElectedType(
        proportional_election=ProportionalElectionElected(
            is_election_result_complete=True,
            list_value=[
                ProportionalElectionElected.List(
                    list_identification='list-id',
                    count_of_seats_gained=1,
                    elected_candidate=[
                        ElectedCandidate(
                            candidate_identification="candidate-id",
                        )
                    ]
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


def test_ech_0252_proporz_election_result_xml(delivery: Delivery) -> None:
    # to xml
    config = SerializerConfig(pretty_print=True)
    serializer = XmlSerializer(config=config)
    xml = serializer.render(delivery)

    # from xml
    parser = XmlParser(context=XmlContext())
    parsed: Delivery = parser.from_string(xml)
    assert delivery == parsed


