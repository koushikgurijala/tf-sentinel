mock "tfplan/v2" {
    module {
        source = "mock-tf2plan-v2-pass.sentinel"
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