function solution( matrix )
    suitable = { }
    total = 0
    
    for i = 1, table.getn( matrix ) do
        for j, v in ipairs( matrix[i] ) do
            if suitable[j]== nil then
                suitable[j] = v
            end
            
            if suitable[j] ~= 0 then
                suitable[j] = v
                total = total + v
            end
        end
    end
    
    return total;
end
