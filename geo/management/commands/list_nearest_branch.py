from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'list nearest branches.'

    def add_arguments(self, parser):
        parser.add_argument('-x', type=float, help='longitude', default=0)
        parser.add_argument('-y', type=float, help='latitude', default=0)
        parser.add_argument('-m', '--limit', type=float, help='limit in meters', default=0)

    def handle(self, *args, **options):
        from geo.models import Branch

        distance_in_meter_tmpl = '111195 * st_distance(point, Point(%s, %s))'
        x = options['x']
        y = options['y']
        limit_in_meter = options['limit']

        params = {
            'select': {
                'id': 'id',
                'distance': distance_in_meter_tmpl,
            },
            'order_by': ['distance'],
            'select_params': (x, y),
        }

        if limit_in_meter > 0:
            params.update({
                'where': [
                    '{} < %s'.format(distance_in_meter_tmpl),
                ],
                'params': (x, y, limit_in_meter),
            })

        objs = Branch.objects.extra(**params)
        for obj in objs:
            print(obj.id, obj.point.x, obj.point.y, obj.distance)
