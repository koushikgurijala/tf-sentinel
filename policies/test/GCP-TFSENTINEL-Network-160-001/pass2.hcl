mock "tfplan/v2" {
    module {
        source = "mock-tfplan-v2-no-network-pass.sentinel"
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