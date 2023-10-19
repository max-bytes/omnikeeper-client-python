from .apiclient import (
    OkApiClient
)

from .layer import (
    create_layer,
    update_layerdata,
    truncate_layer,
)

from .ci import (
    create_ci,
    get_ci_attributes,
)

# import util
from .util import (
    hexString2RGBColor,
)

from .typing import (
    ATTRIBUTETYPE_TEXT,
    ATTRIBUTETYPE_MULTILINE_TEXT,
    ATTRIBUTETYPE_INTEGER,
    ATTRIBUTETYPE_DOUBLE,
    ATTRIBUTETYPE_BOOLEAN,
    ATTRIBUTETYPE_JSON,
)
