import logging
import unittest

from lab_1 import test_gen_file
from lab_1.binary_tree_class import generate_binary_tree, print_binary_tree
from Lab_3.SimpleLogger import SimpleLog

def set_logger():
    main_logger = logging.getLogger(__name__)
    main_logger.setLevel(logging.INFO)

    # настройка обработчика и форматировщика для logger2
    handler = logging.FileHandler(f"Lab_3/{__name__}.log", mode='a')
    formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

    # добавление форматировщика к обработчику
    handler.setFormatter(formatter)
    # добавление обработчика к логгеру
    main_logger.addHandler(handler)

    main_logger.info(f"Testing the custom logger for module {__name__}...")
    return main_logger

if __name__ == '__main__':
    # unittest.main(module=test_gen_file, exit=False)
    main_logger = set_logger()
    logger = SimpleLog()
    tree = generate_binary_tree(height=3, root=14, logger=logger)
    main_logger.info("tree1 was created")
    tree2 = generate_binary_tree(height=-3, root=14)
    main_logger.info("tree2 was created")
    print_binary_tree(tree)
