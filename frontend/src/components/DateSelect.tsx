//Component to allow user to select start and end months

interface DateSelectProps {
    months: string[];
    start: string;
    end: string;
}

export default function DateSelect({months, start, end}: DateSelectProps) {
    return (
        <div>Month Selector - in progress</div>
    )
}