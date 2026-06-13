class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
            "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        def convert(n):
            if n == 0:
                return ""
            if n < 20:
                return below_20[n] + " "
            if n < 100:
                return tens[n // 10] + " " + convert(n % 10)
            return (
                below_20[n // 100]
                + " Hundred "
                + convert(n % 100)
            )

        units = [
            (1_000_000_000, "Billion"),
            (1_000_000, "Million"),
            (1_000, "Thousand"),
            (1, "")
        ]

        res = []

        for value, name in units:
            if num >= value:
                chunk = num // value
                num %= value
                part = convert(chunk).strip()
                if name:
                    res.append(part + " " + name)
                else:
                    res.append(part)

        return " ".join(res)
