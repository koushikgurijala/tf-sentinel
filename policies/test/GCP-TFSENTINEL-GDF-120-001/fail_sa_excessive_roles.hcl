mock "tfplan/v2" {
    module {
        source = "fail_sa_excessive_roles.sentinel"
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