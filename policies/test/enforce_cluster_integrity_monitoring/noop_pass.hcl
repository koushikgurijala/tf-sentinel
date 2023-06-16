mock "tfplan/v2" {
    module {
        source = "mock_tfplan_v2_noop_pass.sentinel"
    }
}

import "module" "tfplan-functions" {
    source = "../../common-functions/tfplan-functions/tfplan-functions.sentinel"
}

test {
    rules = {
        main = true
    }
}