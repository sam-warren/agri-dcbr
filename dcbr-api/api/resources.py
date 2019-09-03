from import_export import resources

from api.models import Registration_Number
from api.models import Operator
from api.models import Address
from api.models import Inspection
from api.models import Operation_Risk_Factor
from api.models import Animal_Risk_Factor
from api.models import Association_Membership


class Registration_NumberResource(resources.ModelResource):
    class Meta:
        model = Registration_Number


class OperatorResource(resources.ModelResource):
    class Meta:
        model = Operator


class AddressResource(resources.ModelResource):
    class Meta:
        model = Address


class InspectionResource(resources.ModelResource):
    class Meta:
        model = Inspection


class Operation_Risk_FactorResource(resources.ModelResource):
    class Meta:
        model = Operation_Risk_Factor


class Animal_Risk_FactorResource(resources.ModelResource):
    class Meta:
        model = Animal_Risk_Factor


class Association_MembershipResource(resources.ModelResource):
    class Meta:
        model = Association_Membership

