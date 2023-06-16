mock "tfplan/v2" {
    module {
        source = "fail_no_custom_sa.sentinel"
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