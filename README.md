#  Filter Values Plugin

A [FiftyOne plugin](https://docs.voxel51.com/plugins/index.html) for filtering
a field of your FiftyOne dataset by one or multiple values simultaneously. 



https://github.com/ehofesmann/filter-values-plugin/assets/21222883/5195638b-add6-466b-944d-1bd6c51369a2




### Installation

If you haven't already,
[install FiftyOne](https://docs.voxel51.com/getting_started/install.html):

```shell
pip install fiftyone
```

Then install the plugin and its dependencies:

```shell
fiftyone plugins download https://github.com/ehofesmann/filter-values-plugin
```


### Usage




1. Load your dataset (in this case the FiftyOne `quickstart` dataset), and
   open the FiftyOne App:

```py
import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("quickstart")

session = fo.launch_app(dataset)
```


2. Select the filter icon in the sample grid.

![Screenshot from 2023-10-30 15-55-49](https://github.com/ehofesmann/filter-values-plugin/assets/21222883/bbed0b1c-c917-4bea-a48f-550ffa237dc9)


3. Select the field by which to filter, copy and paste the value(s), and an
   optional delimiter if a list of values was given. In this example, select
the `uniqueness` field and copy and paste these values:

```py
0.7320790117423479,0.6570019874067852,0.6739862970978517
```

Then enter `,` as the delimiter and hit execute.




https://github.com/ehofesmann/filter-values-plugin/assets/21222883/20a9d1aa-6931-4ed3-ae22-0d63843beca0


https://github.com/ehofesmann/filter-values-plugin/assets/21222883/1dbd1f2d-ca0d-4a84-9035-8093ed393ffe


![Screenshot from 2023-10-30 16-10-20](https://github.com/ehofesmann/filter-values-plugin/assets/21222883/247a533e-ba8b-44e2-a461-e7dff4e7013b)

