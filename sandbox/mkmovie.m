
function run()
    set(0, 'defaultfigurevisible', 'off');
    data = load('sandbox/out.txt');

    % plot(data(:, 1), data(:, 2));

    for t=1:length(data(:, 1))
        t
        figure;
        hold on;
        plot(data(:, 1)(1:t), data(:, 2)(1:t));
        plot(data(:, 1)(t), data(:, 2)(t), 'ro', 'markers', 12);
        plot(data(:, 3)(t), data(:, 4)(t), 'ko', 'markers', 12);
        plot(data(:, 5)(t), data(:, 6)(t), 'ko', 'markers', 12);
        xlim([0 50]);
        ylim([0 50]);
        print(strcat('sandbox/frames/', num2str(t), '.png'));
    end
endfunction

run();
