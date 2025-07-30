#!/opt/julia-1.0.0/bin/julia
#=
Created on Thu Aug 30 21:04:13 2018

@author: tarik

Euler project problem 502
https://projecteuler.net/problem=502

Switched to Julia programming language to run faster.
Works correctly but is still too slow to solve the problem as stated:
    Find (F(1012,100) + F(10000,10000) + F(100,1012)) mod 1 000 000 007
=#
const MAX_W = 10000
const MAX_H = 200
const cache = zeros(Int128, MAX_W, MAX_H, 2, 2)
function castles_max_height(w, h, base, even):Int128
    @assert h>0 #Height should be greater than zero
    @assert w>=-1 #Width should be greater or equal to -1
    if w<=0
        if even
            return 1
        else
            return 0
        end
    elseif h == 1
        if even && !base || !even && base
            return 1
        else
            return 0
        end
    else
        cached_value = cache[w, h, base ? 1 : 2, even ? 1 : 2]
        if cached_value > 0
            return cached_value
        end
        total::Int128 = 0
        for leading_empty = 0:w-1
            for left_width = 1:w-leading_empty
                total+=castles_max_height(left_width, h-1, true, base && !even || !base && even) * castles_max_height(w-leading_empty-left_width-1,h,false,true)
                total+=castles_max_height(left_width, h-1, true, base && even || !base && !even) * castles_max_height(w-leading_empty-left_width-1,h,false,false)
            end
        end
        if base && !even || !base && even
            total+=1
        end

        total = total % 1000000007
        cache[w, h, base ? 1 : 2, even ? 1 : 2] = total
        return total
    end
end

function castles(w, h):Int128
    count1 = castles_max_height(w, h, true, true)
    count2 = castles_max_height(w, h-1, true, true)
    count = (count1 - count2 + 1000000007) % 1000000007
    return count
end

using Dates
time_start = Dates.now()
println("Asserting 4 2")
@assert castles(4,2) == 10
println("Asserting 13 10")
@assert castles(13,10) == 3729050610636 % 1000000007
println("Asserting 10 13")
@assert castles(10,13) == 37959702514 % 1000000007
println("Asserting 100 100")
@assert castles(100,100) == 841913936
println("Verification done")
time_end = Dates.now()
println(time_end - time_start)
