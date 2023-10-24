(defun solution (statues)
    (sort statues '>)
    ( +
        1
        ( -
            ( reduce #'max statues )
            ( reduce #'min statues )
            ( length statues )
        )
    )
)
