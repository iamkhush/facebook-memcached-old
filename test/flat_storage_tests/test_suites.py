test_suites = [ { 'binary_name': "init_test",
                  'cflags': " -DINIT_TEST",
                  'runtime_info': ("do_shell_exec", ["init_test"]) },
                { 'binary_name': "inline_test",
                  'cflags': " -DINLINE_TEST",
                  'runtime_info': ("do_shell_exec", ["inline_test"]) },
                { 'binary_name': "alloc_dealloc_test",
                  'cflags': " -DALLOC_DEALLOC_TEST",
                  'runtime_info': ("do_shell_exec", ["alloc_dealloc_test"]) },
                { 'binary_name': "item_walk_test",
                  'cflags': " -DITEM_WALK_TEST",
                  'runtime_info': ("do_shell_exec", ["item_walk_test"]) },
                { 'binary_name': "paging_test",
                  'cflags': " -DPAGING_TEST",
                  'runtime_info': ("do_shell_exec", ["paging_test"]) },
                { 'binary_name': "assoc_test",
                  'cflags': " -DASSOC_TEST",
                  'runtime_info': ("do_shell_exec", ["assoc_test"]) },
                { 'binary_name': "complex_alloc_test",
                  'cflags': " -DCOMPLEX_ALLOC_TEST",
                  'runtime_info': ("do_shell_exec", ["complex_alloc_test"]), },
                { 'binary_name': "alloc_small_lru_evict_test",
                  'cflags': " -DALLOC_SMALL_LRU_EVICT_TEST",
                  'runtime_info': ("do_shell_exec", ["alloc_small_lru_evict_test"]), },
                { 'binary_name': "alloc_large_lru_evict_test",
                  'cflags': " -DALLOC_LARGE_LRU_EVICT_TEST",
                  'runtime_info': ("do_shell_exec", ["alloc_large_lru_evict_test"]), },
                ]
