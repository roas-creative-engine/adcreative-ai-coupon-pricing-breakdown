#!/usr/bin/env python3
"""
AdCreative.ai Subscription ROI & Annual Billing Discount Calculator 2026.
Computes effective monthly rates, asset generation capacity, and upfront annual savings.
"""
import argparse

def calculate_subscription(monthly_rate, annual_discount_pct):
    annual_base = monthly_rate * 12.0
    discount_multiplier = (100.0 - annual_discount_pct) / 100.0
    annual_billed = annual_base * discount_multiplier
    effective_monthly = annual_billed / 12.0
    annual_savings = annual_base - annual_billed
    return {
        "monthly_rate": monthly_rate,
        "annual_discount_pct": annual_discount_pct,
        "annual_base": annual_base,
        "annual_billed": annual_billed,
        "effective_monthly": effective_monthly,
        "annual_savings": annual_savings
    }

def main():
    parser = argparse.ArgumentParser(description="AdCreative.ai Plan & Annual Discount Calculator")
    parser.add_argument("--monthly-rate", type=float, default=149.0, help="Monthly catalog price in USD (default: $149.00 for Professional)")
    parser.add_argument("--annual-discount", type=float, default=25.0, help="Annual upfront discount percentage (default: 25.0%)")
    args = parser.parse_args()

    res = calculate_subscription(args.monthly_rate, args.annual_discount)
    print(f"Monthly Catalog Rate:    ${res['monthly_rate']:.2f}/mo")
    print(f"Annual Discount Rate:    {res['annual_discount_pct']:.1f}%")
    print(f"Effective Monthly Cost:  ${res['effective_monthly']:.2f}/mo")
    print(f"Annual Billed Total:     ${res['annual_billed']:.2f}")
    print(f"Annual Realized Savings: ${res['annual_savings']:.2f}/year")

if __name__ == "__main__":
    main()
