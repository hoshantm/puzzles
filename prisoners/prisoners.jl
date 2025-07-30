using Random
const DEBUG = false
const PRISONERS = 100
const ATTEMPTS = 50
function tryit()

    a = [1:1:PRISONERS;]
    a = shuffle(a)
    for i in 1:PRISONERS
        if DEBUG
            println("prisoner $i")
        end
        count = 0
        check = i
        while count <= ATTEMPTS
            count += 1
            if a[check] == i
                if DEBUG
                    println("Attempt $count: Checking box $check and found my number")
                end
                break
            else
                if DEBUG
                    println("Attempt $count: Checking box $check and found $(a[check])")    
                end       
                check = a[check]               
            end
        end
           
        if count > ATTEMPTS
            if DEBUG
                println("Prisoner $i failed to find his number in 50 attempts")
            end
            return false
        end
    end
    return true
end

function main()
    tries = 10000000
    success = 0.0
    for i in 1:tries
        if tryit()
            success += 1
        end
    end
    println("Ratio of success = $(success / tries)")
end

main()
 
