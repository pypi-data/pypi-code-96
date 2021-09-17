from rest_framework import (
    serializers,
)

from m3_gar.models import (
    AddhouseTypes,
    AddrObj,
    AddrObjTypes,
    Apartments,
    ApartmentTypes,
    Houses,
    HouseTypes,
    Param,
    ParamTypes,
    ReestrObjects,
    Rooms,
    RoomTypes,
)
from m3_gar.models.hierarchy import (
    AdmHierarchy,
    Hierarchy,
    MunHierarchy,
)
from m3_rest_gar.consts import (
    GAR_DATE_MAX,
)


class ReestrObjectsSerializer(serializers.ModelSerializer):
    """
    Сериализатор сведений об адресном элементе в части его идентификаторов
    """
    class Meta:
        model = ReestrObjects
        fields = '__all__'


class HierarchySerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор сведений по иерархии
    """
    objectid = ReestrObjectsSerializer()
    parentobjid = ReestrObjectsSerializer()

    class Meta:
        model = Hierarchy
        fields = '__all__'


class MunHierarchySerializer(HierarchySerializer):
    """
    Сериализатор сведений по иерархии в муниципальном делении
    """
    class Meta:
        model = MunHierarchy
        fields = '__all__'


class AdmHierarchySerializer(HierarchySerializer):
    """
    Сериализатор сведений по иерархии в административном делении
    """
    class Meta:
        model = AdmHierarchy
        fields = '__all__'


class ParamTypesSerializer(serializers.ModelSerializer):
    """
    Сериализатор сведений по типу параметра
    """
    class Meta:
        model = ParamTypes
        fields = '__all__'


class ParamListSerializer(serializers.ListSerializer):
    """
    Сериализатор списка сведений о классификаторе параметров адресообразующих
    элементов и объектов недвижимости
    """
    def to_representation(self, data):
        data = data.filter(
            enddate=GAR_DATE_MAX,
        ).select_related(
            'typeid',
        )

        return super().to_representation(data)


class ParamSerializer(serializers.ModelSerializer):
    """
    Сериализатор сведений о классификаторе параметров адресообразующих
    элементов и объектов недвижимости
    """
    typeid = ParamTypesSerializer()

    class Meta:
        model = Param
        fields = '__all__'
        list_serializer_class = ParamListSerializer


class AddrObjTypesSerializer(serializers.ModelSerializer):
    """
    Сериализатор сведений по типам адресных объектов
    """
    class Meta:
        model = AddrObjTypes
        fields = '__all__'


class AddrObjSerializer(serializers.ModelSerializer):
    """
    Сериализатор сведений классификатора адресообразующих элементов
    """
    params = ParamSerializer(many=True)
    hierarchy = serializers.SerializerMethodField()

    # На момент описания моделей AddrObjTypes никак не связывается с AddrObj
    # Существующее поле AddrObj.typename - текстовое представление (ул, пер, г, и т.п.)
    # ??? = AddrObjTypesSerializer()

    class Meta:
        model = AddrObj
        fields = '__all__'

    def get_hierarchy(self, obj):
        data = {}

        for name, model in Hierarchy.get_shortname_map().items():
            hierarchy_instance = model.objects.filter(
                objectid=obj.objectid,
                enddate=GAR_DATE_MAX,
                isactive=True,
            ).select_related(
                'objectid',
                'parentobjid',
            ).first()
            hierarchy_serializer = globals()[f'{model.__name__}Serializer']

            if hierarchy_instance and hierarchy_serializer:
                data[name] = hierarchy_serializer(hierarchy_instance).data

        return data


class HouseTypesSerializer(serializers.ModelSerializer):
    """
    Сериализатор сведений по типам домов
    """
    class Meta:
        model = HouseTypes
        fields = '__all__'


class AddhouseTypesSerializer(serializers.ModelSerializer):
    """
    Сериализатор сведений по дополнительным типам домов
    """
    class Meta:
        model = AddhouseTypes
        fields = '__all__'


class HousesSerializer(serializers.ModelSerializer):
    """
    Сериализатор сведений по номерам домов улиц городов и населенных пунктов
    """
    params = ParamSerializer(many=True)
    housetype = HouseTypesSerializer()
    addtype1 = AddhouseTypesSerializer()
    addtype2 = AddhouseTypesSerializer()

    class Meta:
        model = Houses
        fields = '__all__'


class ApartmentTypesSerializer(serializers.ModelSerializer):
    """
    Сериализатор сведений по типам помещений
    """
    class Meta:
        model = ApartmentTypes
        fields = '__all__'


class ApartmentsSerializer(serializers.ModelSerializer):
    """
    Сериализатор сведений по помещениям
    """
    params = ParamSerializer(many=True)
    aparttype = ApartmentTypesSerializer()

    class Meta:
        model = Apartments
        fields = '__all__'


class RoomTypesSerializer(serializers.ModelSerializer):
    """
    Сериализатор сведений по типам комнат
    """
    class Meta:
        model = RoomTypes
        fields = '__all__'


class RoomsSerializer(serializers.ModelSerializer):
    """
    Сериализатор сведений по комнатам
    """
    params = ParamSerializer(many=True)
    roomtype = RoomTypesSerializer()

    class Meta:
        model = Rooms
        fields = '__all__'
