import fiftyone.operators as foo
import fiftyone.operators.types as types
import fiftyone as fo

from fiftyone import ViewField as F


class FilterValues(foo.Operator):
    @property
    def config(self):
        return foo.OperatorConfig(
            name="filter_values",
            label="Filter Values",
            dynamic=True,
        )

    def resolve_placement(self, ctx):
        return types.Placement(
            # Display placement in the actions row of samples grid
            types.Places.SAMPLES_GRID_ACTIONS,
            # Display a button as the placement
            types.Button(
                # label for placement button visible on hover
                label="Filter values",
                icon="/assets/filter.svg",
            )
        )


    def resolve_input(self, ctx):
        inputs = types.Object()

        fields = ctx.dataset.get_field_schema(flat=True)
        field_selector = types.AutocompleteView()
        field_keys = list(fields.keys())
        for key in field_keys:
            field_selector.add_choice(key, label=key)

        inputs.enum(
            "field_name",
            field_keys,
            label="Choose a field",
            description="The field to filter.",
            view=field_selector,
            required=True,
        )

        inputs.str(
            "values",
            label="One or more values by which to filter.",
            view=types.TextFieldView(),
            required=True,
        )

        inputs.str(
            "delimiter",
            label="The delimiter to split by when values is a list. No delimiter indicates a single value is provided.",
            view=types.TextFieldView(),
        )

        return types.Property(
            inputs, view=types.View(label="Filter Field")
        )


    def execute(self, ctx):
        view = ctx.view

        fields = ctx.dataset.get_field_schema(flat=True)
        field_name = ctx.params.get("field_name", None)
        field = fields.get(field_name, None)
        delimiter = ctx.params.get("delimiter", None)
        values = ctx.params.get("values", None)
        if delimiter is None:
            values = [values]
        else:
            values = values.split(delimiter)

        if values is not None and field is not None:
            if isinstance(field, fo.BooleanField):
                values = [bool(v) for v in values]

            elif isinstance(field, fo.IntField):
                values = [int(v) for v in values]

            elif isinstance(field, fo.FloatField):
                values = [float(v) for v in values]

            view = view.match(F(field_name).is_in(values))

        ctx.trigger("set_view", {"view": view._serialize()})


def register(p):
    p.register(FilterValues)
