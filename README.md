#  Filter Values Plugin

A [FiftyOne plugin](https://docs.voxel51.com/plugins/index.html) for filtering
a field of your FiftyOne dataset by one or multiple values simultaneously. 


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


3. Select the field by which to filter, copy and paste the value(s), and an
   optional delimiter if a list of values was given. In this example, select
the `uniqueness` field and copy and paste these values:

```py
0.7320790117423479,0.6570019874067852,0.6739862970978517
```

Then enter `,` as the delimiter and hit execute.
