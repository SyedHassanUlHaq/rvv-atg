import logging
import os
from scripts.test_common_info import *
from scripts.create_test_floating.create_test_common import *

instr = 'vfwmul'


def create_empty_test_vfwmul(xlen, vlen, vsew, lmul, vta, vma, output_dir):
    logging.info("Creating empty test for {}".format(instr))

    path = "%s/%s_empty.S" % (output_dir, instr)
    f = open(path, "w+")

    # Common header files
    print_common_header(instr, f)

    print("  TEST_W_FP_VV_OP( 1,  %s.vv, fmul.d, 0, 1, 1);"%instr, file=f)

    # Common const information
    print_ending(f, generate_data=False)

    f.close()
    os.system("cp %s %s" % (path, output_dir))

    logging.info(
        "Creating empty test for {}: finish in {}!".format(instr, path))

    return path


def create_first_test_vfwmul(xlen, vlen, vsew, lmul, vta, vma, output_dir, rpt_path):
    logging.info("Creating first test for {}".format(instr))

    path = "%s/%s_first.S" % (output_dir, instr)
    f = open(path, "w+")

    # Common header files
    print_common_header(instr, f)

    # Generate macros to test diffrent register
    generate_macros_widen(f, lmul)

    # Generate tests
    num_tests_tuple = generate_tests_widen(instr, f, vsew, lmul, test_wvwf = False)

    # Common const information
    print_common_ending_rs1rs2rd_wvwf(rs1_val, rs2_val, num_tests_tuple, vsew, f, generate_wvwf = False)

    f.close()
    os.system("cp %s %s" % (path, output_dir))

    logging.info(
        "Creating first test for {}: finish in {}!".format(instr, path))

    return path
