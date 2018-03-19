from target import Target
from result import Result
from writer import Writer

target = Target()
result = Result(target.nums)
writer = Writer(target.column, target.nums, result.statusList)
