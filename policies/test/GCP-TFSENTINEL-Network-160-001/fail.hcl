mock "tfplan/v2" {
    module {
        source = "mock-tfplan-v2-fail.sentinel"
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