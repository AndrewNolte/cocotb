# Copyright cocotb contributors
# Licensed under the Revised BSD License, see LICENSE for details.
# SPDX-License-Identifier: BSD-3-Clause

import cocotb


@cocotb.test()
async def test_sv_if(dut):
    """Test that signals in an interface are discovered and iterable"""

    dut.sv_if_i._discover_all()
    assert hasattr(dut.sv_if_i, "a")
    assert hasattr(dut.sv_if_i, "b")
    assert hasattr(dut.sv_if_i, "c")


@cocotb.test(expect_fail=cocotb.SIM_NAME.lower().startswith("xmsim"))
async def test_sv_if_arrays(dut):
    """Test that interface arrays are the correct type and iterable"""

    # should be a HierarchyArrayObject, currently is a NonHierarchyIndexableObject in Xcelium
    print(dut.sv_if_arr)

    assert isinstance(dut.sv_if_arr, cocotb.handle.HierarchyArrayObject)

    dut.sv_if_arr._discover_all()

    m = len(dut.sv_if_arr)
    assert m == 3
    for i in range(m):
        assert hasattr(dut.sv_if_arr[i], "a")
        assert hasattr(dut.sv_if_arr[i], "b")
        assert hasattr(dut.sv_if_arr[i], "c")
