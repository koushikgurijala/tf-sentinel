mock "tfplan/v2" {
    module {
        source = "mock-tf2plan-v2-fail.sentinel"
    }
}

test {
    rules = {
        main = false
    }
}