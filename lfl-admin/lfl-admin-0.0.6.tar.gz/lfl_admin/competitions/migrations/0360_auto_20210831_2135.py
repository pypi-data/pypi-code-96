# Generated by Django 3.2.6 on 2021-08-31 21:35

from django.db import migrations , transaction , connection
from isc_common.common import unknown
from tqdm import tqdm

from lfl_admin.common.models.all_tables import All_tables
from lfl_admin.competitions.models.disqualification_condition import Disqualification_condition
from lfl_admin.competitions.models.disqualification_zones import Disqualification_zones
from lfl_admin.competitions.models.division_stages import Division_stages
from lfl_admin.competitions.models.divisions import Divisions
from lfl_admin.competitions.models.tournaments import Tournaments
from lfl_admin.region.models.regions import Regions


class Migration( migrations.Migration ) :
    dependencies = [
        ('competitions' , '0359_alter_leagues_props') ,
        ('isc_common' , '0125_image_types_c_event') ,
        ('constructions' , '0029_auto_20210829_1347') ,
        ('decor' , '0032_alter_news_images_main_model') ,
        ('inventory' , '0023_alter_clothes_images_main_model') ,
        ('region' , '0068_alter_regions_props') ,
    ]

    def handle( apps , schema_editor ) :

        with transaction.atomic() :
            pbar = tqdm( total=Tournaments.objects.filter( division_id__in=map( lambda x : x.id , Divisions.objects.filter( parent=None ) ) ).exclude( division__code=unknown ).count() )

            for division in Divisions.objects.filter( parent=None ).exclude( code=unknown ) :
                for tournament in Tournaments.objects.filter( division=division ) :
                    # print(tournament.division_round)
                    stage , _ = Division_stages.objects.get_or_create( code=tournament.division_round if tournament.division_round else 0 , defaults=dict( name=f'Этап: {tournament.division_round}' ) )

                    props = 0
                    props_t = tournament.props

                    if division.props.active.is_set :
                        props |= Divisions.props.active
                        props_t != Tournaments.props.active
                    else :
                        props &= ~Divisions.props.active
                        props_t &= ~ Tournaments.props.active

                    if division.props.completed.is_set :
                        props |= Divisions.props.completed
                        props_t &= ~Tournaments.props.active

                    if division.props.favorites.is_set :
                        props |= Divisions.props.favorites
                        props_t |= Tournaments.props.favorites
                    else :
                        props &= ~ Divisions.props.favorites
                        props_t &= ~ Tournaments.props.favorites

                    if division.props.hidden.is_set :
                        props_t |= Tournaments.props.favorites
                        props |= Divisions.props.hidden
                    else :
                        props_t &= ~ Tournaments.props.favorites
                        props &= ~ Divisions.props.hidden

                    division_stage , _ = Divisions.objects.get_or_create(
                        stage=stage ,
                        parent=division ,
                        defaults=dict(
                            name=stage.name ,
                            disqualification_condition=Disqualification_condition.unknown() ,
                            number_of_rounds=0 ,
                            props=props ,
                            region=Regions.unknown() ,
                            zone=Disqualification_zones.unknown()
                        ) )

                    tournament.props = props_t
                    tournament.division = division_stage
                    tournament.save()

                    pbar.update()

    def fill_image_type( apps , schema_editor ) :
        i = 1
        with transaction.atomic() :
            for table in All_tables.objects.filter( table_name__endswith='_images' ).exclude( table_name__in=[ 'common_site_lfl_images' , 'isc_common_images' ] ).order_by( 'table_name' ) :
                print( table.table_name )
                with connection.cursor() as cursor :
                    cursor.execute( f'select id, image_id from {table.table_name}' )
                    rows = cursor.fetchall()
                    for row in rows :
                        id , image_id = row
                        cursor.execute( f'select image_type_id from isc_common_images where id = %s' , [ image_id ] )
                        image_type_rows = cursor.fetchall()
                        for image_type_row in image_type_rows :
                            image_type_id , = image_type_row

                            sql_str = f'update {table.table_name} set type_id = %s where id=%s'
                            cursor.execute( sql_str , [ image_type_id , id ] )
                            print( f'# {i}  {table.table_name}  {[ image_type_id , id ]}' )
                            i += 1

    operations = [
        # migrations.RunPython(handle),
        migrations.RunPython( fill_image_type ) ,
    ]
