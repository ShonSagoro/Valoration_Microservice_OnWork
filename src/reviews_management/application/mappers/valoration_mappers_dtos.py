from reviews_management.application.dtos.request.create_valoration_request import CreateValorationRequest
from reviews_management.application.dtos.request.update_valoration_request import UpdateValorationRequest
from reviews_management.application.dtos.response.valoration_response import ValorationResponse
from reviews_management.domain.entities.comment import CommentRainting
from reviews_management.domain.entities.enum.general_review import GeneralReview
from reviews_management.domain.entities.valoration import Valoration

class ValorationMapperDTO:
    @staticmethod
    def to_domain_valoration_create(valoration_create: CreateValorationRequest) -> Valoration:
        comment = CommentRainting(
            rating=valoration_create.rating,
            comment=valoration_create.comment
        )
        valoration = Valoration(
            comment=comment,
            general_review=GeneralReview.POSITIVE,
            user_uuid=valoration_create.user_uuid,
            provider_uuid=valoration_create.provider_uuid,
        )
        return valoration

    @staticmethod
    def to_domain_valoration_update(valoration_update: UpdateValorationRequest) -> Valoration:
        valoration = Valoration(
            comment=CommentRainting(
                rating=valoration_update.rating,
                comment=valoration_update.comment
            ),
            general_review=GeneralReview.POSITIVE,
            user_uuid="", 
            provider_uuid="", 
        )
        return valoration

    @staticmethod
    def to_response_valoration(valoration: Valoration) -> ValorationResponse:
        return ValorationResponse(
            uuid=str(valoration.uuid),
            rating=valoration.comment.rating,
            comment=valoration.comment.comment,
            user_uuid=valoration.user_uuid,
            general_review=valoration.general_review.value,
            provider_uuid=valoration.provider_uuid,
            createdAt=valoration.createdAt,
            updatedAt=valoration.updatedAt
        ).to_dict()
