from typing import TypeVar, Any, Sequence, Mapping, Callable, Generator, Final, Literal, Union, List, Dict, Tuple, Set

# Corrected variable assignment with integer type
variable_name: int = int(10 / 2)

# Corrected function to use addition instead of unsupported subtraction with strings
def fmt(value: str, excitement: int = 10) -> str:
    return value + "!" * excitement

# Fixed argument to match expected type
fmt('Hello', 10)

# Corrected type to be compatible with possible None values
my_age: Union[int, float, None] = None
my_city: Union[str, None] = None

# Changed number to a valid type alias and corrected prices to a List
Number = Union[int, float]
prices: List[Number] = [100, 105, 125.5]

# Corrected typing for the image variable
Image = List[List[int]]
image: Image = [[0] * 1000]

# Typing corrected for dictionary with generic int key and any type
T1 = TypeVar('T1')
DictWithIntKey = Dict[int, T1]

a: DictWithIntKey[str] = {0: 'zero', 1: 'one'}
b: DictWithIntKey[bool] = {0: False, 1: True}
c: DictWithIntKey[int] = {0: 0, 1: 1}
d: DictWithIntKey[float] = {0: 0.0, 1: 1.0}

# Fixed type annotations for function parameters
T2 = TypeVar('T2')
def combine(a: T2, b: T2) -> str:
    return str(a) + str(b)

# Test calls to combine function with matching types
print(combine(10, 20))
print(combine('hello', 'world'))

# Corrected list and tuple annotations
lst_1: List[Union[int, str]] = [1, "2"]
lst_2: List[int] = [1, 2, 3, 4]
lst_3: List[List[int]] = [[1, 2], [3, 4]]

tpl_1: Tuple[int, ...] = (1, 2, 3, 4)
tpl_2: Tuple[List[int], List[str]] = ([1, 2], ['1', '2'])
tpl_3: Tuple[List[int], List[int]] = ([1, 2], [3, 4])
tpl_4: Tuple[int, ...] = (1, 2, 3, 4)

# Corrected dict typing
dt_1: Dict[str, int] = {"a": 1, "b": 2}

# Fixed set annotation
st_1: Set[Union[int, str]] = {1, 2, '3', '4'}

# Corrected type annotations in functions
def get_first(items: List[Any]) -> Any:
    return items[0]

get_first(['1', 1])

def first_element(items: Sequence[Any]) -> Any:
    return items[0]

first_element((1, 2, 3))

def get_value(data: Mapping[str, Any], key: str) -> Any:
    return data.get(key)

get_value({'1': 2.0, '3': 4.0}, key='1')

# Corrected callable type syntax
def is_twice_as_big(num1: int, num2: int) -> bool:
    return num1 >= 2 * num2

def compare_nums(num1: int, num2: int, comp: Callable[[int, int], bool]) -> int:
    if comp(num1, num2):
        return num1
    else:
        return num2

compare_nums(10, 3, is_twice_as_big)

# Added generator type annotation
def do_twice() -> Generator[int, None, None]:
    yield 1
    yield 2

# Corrected return type annotation for play function to match None return type
def play(player_name: str) -> None:
    print(f"Хід {player_name}")

play("Іван")

# Fixed division return type to float
def calc_div(a: int, b: int) -> float:
    return a / b

# Added typing for Literal and corrected function
ReadOnlyMode = Literal["r", "r+"]

def read_file(file_name: str, mode: ReadOnlyMode) -> None:
    pass

read_file('data.txt', 'r')

# Fixed Final usage
MAX_SIZE: Final = 1_000
# MAX_SIZE += 1 # This line is removed because MAX_SIZE is immutable due to Final type
