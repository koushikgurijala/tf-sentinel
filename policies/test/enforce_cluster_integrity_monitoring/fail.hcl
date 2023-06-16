mock "tfplan/v2" {
    module {
        source = "mock_tfplan_v2_fail.sentinel"
    }
}

import "module" "tfplan-functions" {
    source = "../../common-functions/tfplan-functions/tfplan-functions.sentinel"
}

test {
    rules = {
        main = false
    }
}