require 'gnuplot.rb'

Gnuplot.open do |gp|
  Gnuplot::Plot.new( gp ) do |plot|
    plot.output "Sin Wave.pdf"
    plot.terminal "pdf colour size 27cm,19cm"

    plot.xrange "[-10:10]"
    plot.title  "Sin/Cos Wave Example"
    plot.ylabel "x"
    plot.xlabel "sin(x)"

    plot.data << Gnuplot::DataSet.new( "sin(x)" ) do |ds|
      ds.with = "lines"
      ds.linewidth = 4
    end

    plot.data << Gnuplot::DataSet.new( "cos(x)" ) do |ds|
      ds.with = "linespoints"
      ds.linewidth = 4
    end
  end
end