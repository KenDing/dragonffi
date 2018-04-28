# Copyright 2018 Adrien Guinet <adrien@guinet.me>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# RUN: "%python" "%s" | "%FileCheck" "%s"

import pydffi
FFI = pydffi.FFI()
CU = FFI.compile('''
#include <stdio.h>
typedef int int2[2];
int foo(int2* ar)
{
    printf("%d %d\\n", ar[0][0], ar[0][1]);
}
''')

v = CU.types.int2()
v.set(0, 1)
v.set(1, 2)
# CHECK: 1 2
CU.funcs.foo(FFI.ptr(v))

v[0] = 10
v[1] = 20
# CHECK: 10 20
CU.funcs.foo(FFI.ptr(v))