using DataStructures
using Query
using ProgressBars

mutable struct Node{T}
    quantities::Vector{T}
    parent::Union{Node{T}, Nothing}
# TODO: Implement show function
end

function visited(node::Node{T}, quantities::Vector{T}) :: Bool where T <: Integer
    while true
        if node.quantities == quantities
            return true
        elseif node.parent === nothing
            return false
        else
            node = node.parent
        end
    end
end

function gen_solution_found(final_quantities::Vector{T}) where T <: Integer
    groups = @groupby(_)(final_quantities)
    qs = [key(g) for g in groups]
    ns = [length(values(g)) for g in groups]
    function solution_found(quantities::Vector{T}) :: Bool
        all(i -> count(q -> q == qs[i], quantities) == ns[i], 1:length(qs))
    end
end

function gen_solution(solution_node::Node{T}) :: Vector{Vector{T}} where T
    solution_quantities_list=Vector{Vector{T}}(undef, 0)
    while true
        push!(solution_quantities_list, solution_node.quantities)
        solution_node = solution_node.parent
        if solution_node === nothing
            break
        end
    end

    reverse!(solution_quantities_list)
    return solution_quantities_list
end

function solver(capacities::Vector{T}, initial_quantities::Vector{T}, final_quantities::Vector{T}; allow_empty=false, allow_fill=false, n_solutions=1) where T <: Integer
    @debug "Capacities:\n$capacities"
    @debug "Initial Quantities:\n$initial_quantities"
    @debug "Final quantities:\n$final_quantities"
    solution_found = gen_solution_found(final_quantities)

    node_queue = Queue{Node{T}}()
    enqueue!(node_queue, Node{T}(initial_quantities, nothing))
    solutions = Vector{Vector{Vector{T}}}(undef, 0)
    while length(node_queue) > 0 && length(solutions) < n_solutions
        current_node = dequeue!(node_queue)
        current_quantities = current_node.quantities
        for (i, q_from) in enumerate(current_quantities)
            for (j, q_to) in enumerate(current_quantities)
                capacity_to = capacities[j]
                if i != j && q_from != 0 && q_to < capacity_to
                    new_quantities = copy(current_quantities)
                    q_transfer = min(capacity_to - q_to, q_from)
                    new_quantities[i]-=q_transfer
                    new_quantities[j]+=q_transfer
                    if !visited(current_node, new_quantities)
                        new_node = Node{T}(new_quantities, current_node)
                        if solution_found(new_quantities)
                            @debug "Solution found:\n$new_quantities"
                            push!(solutions, gen_solution(new_node))
                        else
                            @debug "New node with quantities:\n$new_quantities"
                            enqueue!(node_queue, new_node)
                        end
                    end
                end
            end

            if allow_empty && q_from > 0
                new_quantities = copy(current_quantities)
                new_quantities[i] = 0
                if !visited(current_node, new_quantities)
                    new_node = Node{T}(new_quantities, current_node)

                    if solution_found(new_quantities)
                        push!(solutions, gen_solution(new_node))
                    else
                        enqueue!(node_queue, new_node)
                    end
                end
            end

            if (allow_fill && q_from < capacities[i])
                new_quantities = current_quantities.copy()
                new_quantities[i] = capacities[i]
                if !visited(current_node, new_quantities)
                    new_node = Node{T}(new_quantities, current_node)

                    if solution_found(new_quantities)
                        push!(solutions, gen_solution(new_node))
                    else
                        enqueue!(node_queue, new_node)
                    end
                end
            end
        end
    end
    solutions
end

function solve(capacities::Vector{T}, initial_quantities::Vector{T}, final_quantities::Vector{T}, allow_empty=false, allow_fill=false) where T <: Integer
    solutions = solver(capacities, initial_quantities, final_quantities, allow_empty=allow_empty, allow_fill=allow_fill, n_solutions=1)
    if length(solutions) == 1
        return solutions[1]
    else
        return nothing
    end
end

function solve_and_print(capacities::Vector{T}, initial_quantities::Vector{T}, final_quantities::Vector{T}; allow_empty=false, allow_fill=false, n_solutions=1) where T <: Integer
    solutions = solver(capacities, initial_quantities, final_quantities, allow_empty=allow_empty, allow_fill=allow_fill)
    i = 0
    for solution in solutions
        if solution !== nothing
            println("Solution found in $(length(solution)-1) moves.")
            for (move, quantities) in enumerate(solution)
                println("$move - $quantities")
            end
            println(' ' ^ 20)
        else
            if i==0
                println("No solution found.")
            elseif i+1<n_solutions
                print("Only $(i+1) solutions found")
            end
            break
        end
        i+=1
        if i >= n_solutions
            break
        end
    end
end

function solve_standard_problem(n_solutions::Int)
    capacities=[8, 5, 3]
    initial_quantities=[8, 0, 0]
    final_quantities = [4, 4]
    solve_and_print(capacities, initial_quantities, final_quantities, n_solutions=n_solutions)
end

function find_toughest()
    capacities = [13, 7, 5]
    max_total_quantity = sum(capacities)-1
    max_steps = 0
    for i in ProgressBar(min(capacities[1], max_total_quantity):-1:0)
        for j in min(capacities[2], max_total_quantity-i):-1:0
            for k in min(capacities[3], max_total_quantity-i-j):-1:0
                initial_quantities = [i, j, k]
                total_quantity = sum(initial_quantities)
                for l in 0:min(capacities[1], max_total_quantity)
                    for m in 0:min(capacities[2], max_total_quantity-l)
                        n = total_quantity - l - m
                        if n > capacities[3]
                            continue
                        end
                        final_quantities = [l, m, n]
                        solution = solve(capacities, initial_quantities, final_quantities)
                        if (solution !== nothing && length(solution) > max_steps)
                            max_steps = length(solution)
                            println("$(max_steps-1) steps")
                            println(capacities)
                            println(initial_quantities)
                            println(final_quantities)
                            println('-'^20)
                        end
                    end
                end
            end
        end
    end
end

function main()
    solve_standard_problem(3)
    find_toughest()
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
