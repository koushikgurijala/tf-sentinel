mock "tfplan/v2" {
    module {
        source = "mock-tf2plan-v2-pass.sentinel"
    }
}

test {
    rules = {
        main = true
    }
}